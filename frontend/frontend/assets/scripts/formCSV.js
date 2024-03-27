const form = document.getElementById('myForm');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // Verhindert das Standardverhalten des Formulars

  // Hier kannst du den Code zum Speichern der Daten in eine Datenbank oder CSV-Datei einfügen

  // Beispielcode zum Abrufen der eingegebenen Werte
  const alter = document.querySelector('input[name="alter"]').value;
  const tageSymptome = document.querySelector('input[name="tageSymptome"]').value;
  const geschlecht = document.querySelector('select[name="geschlecht"]').value;
  const groesse = document.querySelector('input[name="groesse"]').value;
  const gewicht = document.querySelector('input[name="gewicht"]').value;
  const raucher = document.querySelector('select[name="raucher"]').value;
  const symptome = document.querySelector('textarea[name="symptome"]').value;

  // Beispielcode zum Erstellen einer CSV-Zeichenkette mit den Daten
  const csvData = `"Alter","Tage Symptome","Geschlecht","Größe in cm","Gewicht in kg","Raucher","Symptome"\n`;
  const newRow = `"${alter}","${tageSymptome}","${geschlecht}","${groesse}","${gewicht}","${raucher}","${symptome}"\n`;
  const csvContent = csvData + newRow;

  // Beispielcode zum Erstellen und Herunterladen der CSV-Datei
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'formular_data.csv';
  link.click();

  // Erfolgsmeldung anzeigen
  const successMessage = document.createElement('p');
  successMessage.textContent = 'Die Daten wurden erfolgreich gesendet.';
  successMessage.classList.add('success-message');
  form.appendChild(successMessage);

  // Input-Felder zurücksetzen
  form.reset();
});
