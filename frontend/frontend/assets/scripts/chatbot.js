// This function will get the data from the last page and write it in the text input
window.onload = function() {
  const form = document.getElementById('chat-form');
  const input = form.querySelector('.user-entry__input');
  input.value = localStorage.getItem("Transfer");

  // if needed to make the user prevent another symptome
 // input.disabled = true;
};

// To print a funny msg, when the user change to another tab.
let titl = document.title;
window.addEventListener("blur", () => {
  document.title = "Where did u go ! :("
})
window.addEventListener("focus", () => {
  document.title = titl;
})

/*
const form = document.getElementById('chat-form');
const input = form.querySelector('.user-entry__input');
// when the button clicked take the input and choose a random diseases
    form.addEventListener('submit', (event) => {
      event.preventDefault();

      const userMessage = input.value;
      const diseases = [
        "COVID-19",
        "Malaria",
        "Ebola",
        "Cholera",
        "Tuberculosis",
        "Measles",
        "Yellow fever",
        "HIV/AIDS",
        "Hepatitis B",
        "Influenza",
        "Dengue fever",
        "Polio",
        "Zika virus",
        "Chikungunya",
        "Lyme disease",
        "Leptospirosis",
        "Typhoid fever",
        "Meningitis",
        "Pneumonia",
        "Bronchitis",
        "Asthma",
        "Cancer",
        "Alzheimer's disease",
        "Parkinson's disease",
        "Multiple sclerosis",
        "Crohn's disease",
        "Ulcerative colitis",
        "Diabetes",
        "Heart disease",
        "Stroke"
      ];
      const ran = Math.floor(Math.random() * diseases.length);
      const answer = diseases[ran]; // choose a random disease from the above array as an answer
      const chatWindow = document.querySelector('.form-window');

      // print the user message
      const userBubble = document.createElement('div');
      userBubble.classList.add('pat-bubble');
      userBubble.textContent = userMessage;
      chatWindow.appendChild(userBubble);

      // print the answer
      const replyBubble = document.createElement('div');
      replyBubble.classList.add('pat-bubble', 'bot-bubble');
      replyBubble.textContent = `You maybe have: ${answer}`;
      chatWindow.appendChild(replyBubble);

      // clear the input field after getting response, so he can make a new input
      input.value = '';
    }); */






  // The same thing but with server, we can use our Model
 
  const form = document.getElementById('chat-form');
  const input = form.querySelector('.user-entry__input');
  
  form.addEventListener('submit', (event) => {
    event.preventDefault();
  
    const userMessage = input.value;
    const url = '/analyse'; // API endpoint URL
    const chatWindow = document.querySelector('.form-window');
  
    // Make API call to get a response
    fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symptome: userMessage }) // Send Patient's Symptome as JSON data
    })
    
      .then (response => response.json())
      .then(data => {
        const { response } = data;; // Extract the quote from the API response
  
        // Print the user message
        const userBubble = document.createElement('div');
        userBubble.classList.add('pat-bubble');
        userBubble.textContent = userMessage;
        chatWindow.appendChild(userBubble);
  
        // Print the answer from the NLP
        const replyBubble = document.createElement('div');
        replyBubble.classList.add('pat-bubble', 'bot-bubble');
        replyBubble.textContent = `The predicated Model Sagte :\n\n "${response}"`;
        chatWindow.appendChild(replyBubble);
      })
      .catch(error => {
        console.error('There was a problem with the network request:', error);
      });
  
    // Clear the input field
    input.value = '';
  });