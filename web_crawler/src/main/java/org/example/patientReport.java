package org.example;
public class patientReport {
    private String Diagnosis ;
    private String Text;


        // getters and setters omitted for brevity...

        @Override
        public String toString() {
            return "{ \"url\":\"" + Diagnosis + "\", "
                    + "\"price\": \"" + Text + "\" }";
        }

    public void setText(String text) {
        Text = text;
    }

    public void setDiagnosis(String diagnosis) {
        Diagnosis = diagnosis;
    }
}
