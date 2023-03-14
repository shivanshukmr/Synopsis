async function sendRequest() {
  const inputValue = document.getElementById('mainInput').value;
  const payload = getPayload(inputValue);

  console.log(payload);

  const url = new URL('/api/summary', window.location.href);
  url.search = new URLSearchParams(payload).toString();

//   // create loading symbol
//   const loading = document.createElement("div");
//   loading.classList = "loader position-absolute top-50 start-100 translate-middle";
//   document.body.appendChild(loading);

//   const circle1 = document.createElement("div");
//   const circle2 = document.createElement("div");


  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });
  const data = await response.json();

  return data;
}

function getPayload(value) {
  const httpURL = /http:\/\//;
  const httpsURL = /https:\/\//;
  let payload = {};

  if (httpURL.test(value) || httpsURL.test(value)) {
    payload.url = value;
  } else {
    payload.text = value;
  }

  return payload;
}

function onpress() {
  sendRequest().then((result) => {
    const inputDiv = document.getElementById("inputDiv");
    inputDiv.parentNode.removeChild(inputDiv);

    const outputDiv = document.createElement("div");
    outputDiv.classList = "position-absolute top-50 start-50 translate-middle container col-sm-10-mx-auto row card card-body input-group text-center";
    outputDiv.id = "outputDiv";

    // const innerOutputDiv = document.createElement("div");
    // innerOutputDiv.classList = "";
    // outputDiv.style = "alignment: center;";

    const outputPara = document.createElement("p");
    outputPara.classList = "card-text";
    outputPara.style = "text-center;";
    outputPara.innerHTML = result.text;

    outputDiv.appendChild(outputPara);
    document.body.appendChild(outputDiv);
  });
};
