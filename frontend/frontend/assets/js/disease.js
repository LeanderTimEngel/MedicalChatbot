// Ein leeres Objekt erstellen, um die Krankheitszählungen zu speichern
let diseaseCounts = {};

Papa.parse("/data/Data1.csv", {
    download: true,
    header: true,
    complete: function(row) {
        let disease = row.data[1];

        // Wenn die Krankheit bereits im diseaseCounts-Objekt existiert, erhöhen Sie den Zähler
        if (disease in diseaseCounts) {
            diseaseCounts[disease]++;
        }
        // Ansonsten fügen Sie die Krankheit zum diseaseCounts-Objekt hinzu und setzen Sie den Zähler auf 1
        else {
            diseaseCounts[disease] = 1;
        }
        
        // Die Krankheiten und ihre Zählungen in Arrays umwandeln, die von Chart.js verwendet werden können
        let diseases = Object.keys(diseaseCounts);
        let counts = Object.values(diseaseCounts);
        
        // Rufen Sie die Funktion zum Erstellen des Diagramms auf
        createChartDisease(diseases, counts);
    }
});