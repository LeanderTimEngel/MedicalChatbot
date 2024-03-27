// Ein leeres Objekt erstellen, um die Krankheitszählungen zu speichern
let diseaseCounts = {};

// Zeigen Sie das Ladeelement an
document.getElementById("loading").style.display = "block";

// CSV-Datei mit Papa Parse parsen
Papa.parse("/data/Data1.csv", {
  download: true,
  step: function (row) {
    // Die Krankheit aus der aktuellen Zeile extrahieren
    let disease = row.data[1];

    // Wenn die Krankheit bereits im diseaseCounts-Objekt existiert, erhöhen Sie den Zähler
    if (disease in diseaseCounts) {
      diseaseCounts[disease]++;
    }
    // Ansonsten fügen Sie die Krankheit zum diseaseCounts-Objekt hinzu und setzen Sie den Zähler auf 1
    else {
      diseaseCounts[disease] = 1;
    }
  },
  complete: function () {
    // Verbergen Sie das Ladeelement
    document.getElementById("loading").style.display = "none";

    // Die Krankheiten und ihre Zählungen in Arrays umwandeln, die von Chart.js verwendet werden können
    let diseases = Object.keys(diseaseCounts);
    let counts = Object.values(diseaseCounts);

    // Ein neues Diagramm erstellen
    let ctx = document.getElementById("myChart").getContext("2d");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: diseases,
        datasets: [
          {
            data: counts,
            backgroundColor: [
              "#ff6384",
              "#36a2eb",
              "#cc65fe",
              "#ffce56",
              "#2eb82e",
              "#2e33b8",
              "#b82e2e",
            ],
            hoverBackgroundColor: [
              "#ff6384",
              "#36a2eb",
              "#cc65fe",
              "#ffce56",
              "#2eb82e",
              "#2e33b8",
              "#b82e2e",
            ],
          },
        ],
      },
      options: {
        plugins: {
          legend: {
            labels: {
              // Ändert die Schriftfarbe der Legendenbeschriftungen
              color: "white",
            },
          },
        },
      },
    });
  },
});
