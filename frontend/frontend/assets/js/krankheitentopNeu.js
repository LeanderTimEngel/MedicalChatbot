// Ein leeres Objekt erstellen, um die Krankheitszählungen zu speichern
let diseaseCounts = {};

// Anzahl der insgesamt gelesenen Zeilen (oder Datenpunkte)
let totalDataPoints = 0;

// CSV-Datei mit Papa Parse parsen
Papa.parse("/frontend/data/Data1.csv", {
  download: true,
  step: function (row) {
    // Die Krankheit aus der aktuellen Zeile extrahieren
    let disease = row.data[1];

    // Erhöhen Sie den Gesamtzähler für die Datenpunkte
    totalDataPoints++;

    if (disease && disease.trim() !== "") {
      // Wenn die Krankheit bereits im diseaseCounts-Objekt existiert, erhöhen Sie den Zähler
      if (disease in diseaseCounts) {
        diseaseCounts[disease]++;
      }
      // Ansonsten fügen Sie die Krankheit zum diseaseCounts-Objekt hinzu und setzen Sie den Zähler auf 1
      else {
        diseaseCounts[disease] = 1;
      }
    }
  },
  complete: function () {
    // Verbergen Sie das Ladeelement
    document.getElementById("loading").style.display = "none";

    // Sortieren Sie die Krankheiten nach ihren Zählungen
    let sortedDiseases = Object.keys(diseaseCounts).sort(
      (a, b) => diseaseCounts[b] - diseaseCounts[a]
    );
    let sortedCounts = sortedDiseases.map((disease) => diseaseCounts[disease]);

    // Ermitteln Sie die häufigste und seltenste Krankheit und die Anzahl der verschiedenen Krankheiten
    let mostCommonDisease = sortedDiseases[0];
    let leastCommonDisease = sortedDiseases
      .filter((disease, index) => sortedCounts[index] >= 5)
      .slice(-1)[0];
    let numDifferentDiseases = sortedDiseases.length;

    // Diese Werte im DOM anzeigen
    document.getElementById("totalDataPoints").innerHTML = totalDataPoints;
    document.getElementById("numDifferentDiseases").textContent =
      numDifferentDiseases;
    document.getElementById("mostCommonDisease").textContent =
      mostCommonDisease;
    document.getElementById("leastCommonDisease").textContent =
      leastCommonDisease;

    // Extrahieren Sie die 5 häufigsten Krankheiten und ihre Zählungen
    let top5Diseases = sortedDiseases.slice(0, 5);
    let top5Counts = sortedCounts.slice(0, 5);

    // Extrahieren Sie die 5 seltensten Krankheiten (die mindestens 5 Mal vorkommen) und ihre Zählungen
    let filteredDiseases = sortedDiseases.filter(
      (disease, index) => sortedCounts[index] >= 5
    );
    let filteredCounts = sortedCounts.filter((count) => count >= 5);

    let bottom5Diseases = filteredDiseases.slice(-5);
    let bottom5Counts = filteredCounts.slice(-5);

    // Erstellen Sie Diagramme für die 5 häufigsten und 5 seltensten Krankheiten
    let myChartInstance = createChart("myChart", sortedDiseases, sortedCounts, "bar");
    createChart("top5Chart", top5Diseases, top5Counts, "pie");
    createChart("bottom5Chart", bottom5Diseases, bottom5Counts, "pie");
  },
});

// Klick-Event-Handler
document.getElementById("changeChartType").addEventListener("click", function() {
  // Diagrammtyp ändern
  myChartInstance.config.type = myChartInstance.config.type === 'pie' ? 'bar' : 'pie';

  // Diagramm aktualisieren
  myChartInstance.update();
});

// Erstellen Sie eine Funktion, um ein Diagramm zu erstellen
function createChart(canvasId, diseases, counts, chartType) {
  if (!diseases.length || !counts.length) {
    return;
  }
  let ctx = document.getElementById(canvasId).getContext("2d");
  new Chart(ctx, {
    type: chartType,
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
}
