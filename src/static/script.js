function onpress() {
    const inputValue = document.getElementById('mainInput').value;
    console.log(inputValue);
    const payload = {
      url: inputValue,
    };
  
    const url = new URL('/api/summary', window.location.href);
    url.search = new URLSearchParams(payload).toString();
  
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
  }
  