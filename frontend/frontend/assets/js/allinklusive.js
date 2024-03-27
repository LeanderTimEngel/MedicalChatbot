// Ein leeres Objekt erstellen, um die Krankheitszählungen zu speichern
let diseaseCounts = {};

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
    // Die Krankheiten und ihre Zählungen in Arrays umwandeln, die von Chart.js verwendet werden können
    let diseases = Object.keys(diseaseCounts);
    let counts = Object.values(diseaseCounts);

    // Die Krankheiten nach ihren Zählungen sortieren
    let sortedIndices = Array.from(counts.keys()).sort((a, b) => counts[b] - counts[a]);
    let sortedDiseases = sortedIndices.map(i => diseases[i]);
    let sortedCounts = sortedIndices.map(i => counts[i]);

    // Extrahieren Sie die Top 5 häufigsten und seltensten Krankheiten und ihre Zählungen
    let top5Diseases = sortedDiseases.slice(0, 5);
    let top5Counts = sortedCounts.slice(0, 5);
    let bottom5Diseases = sortedDiseases.slice(-5);
    let bottom5Counts = sortedCounts.slice(-5);

    // Diagramme erstellen
    createChart('myChart', diseases, counts);
    createChart('top5Chart', top5Diseases, top5Counts);
    createChart('bottom5Chart', bottom5Diseases, bottom5Counts);
  }
});

function createChart(canvasId, labels, data) {
  let ctx = document.getElementById(canvasId).getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          data: data,
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
}
