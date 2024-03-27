import sys

import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from spellchecker import SpellChecker
from collections import Counter
import time
if 'numpy.core._overrides' not in sys.modules:
    import numpy

# Load the CSV file
csv_file_path = sys.argv[1]  # Get the CSV file path from the command-line argument
df = pd.read_csv(csv_file_path)

# Remove duplicate rows based on the 'label' and 'text' columns
df.drop_duplicates(subset=['label', 'text'], inplace=True)

# Spell checking function
spell = None  # Declare the spell-checker object as a global variable

def initialize_spell_checker():
    global spell
    spell = SpellChecker()

def spell_check(text):
    if isinstance(text, str):
        words = str(text).split()
        corrected_words = []

        # Check if word is in the dictionary and handle None case
        for word in words:
            corrected_word = spell.correction(word)
            if corrected_word is not None:
                corrected_words.append(corrected_word)

        corrected_text = ' '.join(corrected_words)
        return corrected_text
    else:
        return text

def process_chunk(chunk):
    # Spell check the 'text' column
    chunk['text'] = chunk['text'].apply(spell_check)

    # Count the occurrence of words in the chunk using Counter
    chunk_counts = Counter(' '.join(chunk['text']).split())

    # Convert chunk_counts to a DataFrame
    chunk_counts_df = pd.DataFrame.from_dict(chunk_counts, orient='index', columns=['count'])

    # Filter out words that occur more than 80% of texts using pandas' vectorized operations
    valid_words_df = chunk_counts_df[chunk_counts_df['count'] / len(chunk) <= 0.8]

    # Get the set of valid words
    valid_words = set(valid_words_df.index)

    # Filter out words that occur more than 80% of texts using pandas' vectorized operations
    chunk['text'] = chunk['text'].apply(lambda text: ' '.join([word for word in str(text).split() if word in valid_words]))

    return chunk

# Measure the running time
start_time = time.time()

# Before creating the pool, initialize the spell-checker object
initialize_spell_checker()

# Split the dataframe into chunks for processing
num_cores = min(cpu_count(), len(df))
chunk_size = int(np.ceil(len(df) / num_cores))
df_chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

# Process each chunk in parallel
pool = Pool(processes=num_cores)
processed_chunks = list(tqdm(pool.imap(process_chunk, df_chunks), total=len(df_chunks)))
pool.close()
pool.join()

# Concatenate the processed chunks back into a single dataframe
df_cleaned = pd.concat(processed_chunks)

# Count total rows
total_rows = len(df_cleaned)

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)

# Calculate the running time
end_time = time.time()
running_time = end_time - start_time
print("Running time: {:.2f} seconds".format(running_time))
