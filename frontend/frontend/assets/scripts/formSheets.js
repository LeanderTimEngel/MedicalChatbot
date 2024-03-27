document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var data = {
      alter: e.target.elements[0].value,
      tageSymptome: e.target.elements[1].value,
      geschlecht: e.target.elements[2].value,
      groesse: e.target.elements[3].value,
      gewicht: e.target.elements[4].value,
      raucher: e.target.elements[5].value,
      symptome: e.target.elements[6].value,
    };
  
    fetch('https://script.google.com/macros/s/AKfycbwCmcyVkYiWxmPdnNMCN7HjqVp4T-LM6blXZbwXMTBb9RnZNCtnT23JCmtpib781KfQ/exec', {
      method: 'POST',
      mode: 'no-cors',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
  });