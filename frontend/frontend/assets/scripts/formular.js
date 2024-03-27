document.getElementById('analyseFormular').addEventListener('submit', function(event) {
    // Abbrechen durch browser
    event.preventDefault();
  
    var name = event.target.elements[0].value;
    var email = event.target.elements[1].value;
    var symptome = event.target.elements[2].value;
  
    var data = {
      name: name,
      email: email,
      symptome: symptome
    };
  
    // Sendet Daten als POST-Anfrage ans Backend - Fiktive URL :D :D
    fetch('/speichern', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Erfolgreich:', data);
    })
    .catch((error) => {
      console.error('Fehler:', error);
    });
  });