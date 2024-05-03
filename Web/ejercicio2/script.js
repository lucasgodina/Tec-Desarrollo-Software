function calcular() {
  let talle = document.getElementById("talle").value;
  let tela = document.getElementById("tela").value;
  let total = 0;

  switch (talle) {
    case "s":
      total = 50000;
      break;
    case "m":
      total = 70000;
      break;
    case "l":
      total = 90000;
      break;
    case "xl":
      total = 120000;
      break;
    case "xxl":
      total = 150000;
      break;
    default:
      break;
  }
  if (tela == "seda") {
    total += total * 0.4;
  } else if (tela == "lycra") {
    total += total * 0.2;
  }
  return total;
}

function calcularUnidad() {
  document.getElementById("precio-final").innerHTML = calcular();
}

function calcularMayorista() {
  document.getElementById("precio-final").innerHTML = calcular() * 0.9;
}

/*function encaje() {
  let imagen = document.getElementById("imagen-vestido");
  if (document.getElementById("encaje").checked) {
    imagen.src = "./vestido-con-encaje.jpg";
  } else {
    imagen.src = "./vestido-sin-encaje.jpg";
  }
}
*/
