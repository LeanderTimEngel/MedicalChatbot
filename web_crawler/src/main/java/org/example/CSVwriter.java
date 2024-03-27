package org.example;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class CSVwriter {
    private String filePath;

    public CSVwriter(String filePath) {
        this.filePath = filePath;
    }
    int i = 0;
    public void writeRow(int number, String label, String text) {

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {

            // Write the data row
            String data = String.format("%d,\"%s\",\"%s\"\n", number, label, text);
            writer.write(data);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
