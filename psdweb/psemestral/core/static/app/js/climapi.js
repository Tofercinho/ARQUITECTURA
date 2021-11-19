
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');



fetch('https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&appid=92193a0bddde1d5ebcc9787c63185f53&lang=sp')
.then(response => response.json())
.then(data => {
  var tempValue = ((data['main']['temp'])-268.2).toFixed(1);
  var nameValue = data['name'];
  var descValue = data['weather'][0]['description'];

  main.innerHTML = nameValue;
  desc.innerHTML = "Actualmente hay: "+descValue;
  temp.innerHTML = "Temperatura - "+tempValue+"°C";

})

