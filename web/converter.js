// The page's only logic: read Fahrenheit, show Celsius.
function fahrenheitToCelsius(fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

document.getElementById("converter").addEventListener("submit", function (event) {
  event.preventDefault();
  var fahrenheit = Number(document.getElementById("fahrenheit").value);
  var celsius = fahrenheitToCelsius(fahrenheit);
  document.getElementById("result").textContent =
    fahrenheit + " °F is " + celsius.toFixed(2) + " °C";
});
