const hamburger = document.querySelector('.hamburger');
const navLink = document.querySelector('.nav__link');

hamburger.addEventListener('click', () => {
	navLink.classList.toggle('hide');
});

/*
Call a function when a button is clicked:
    <button onclick="myFunction()">Click me</button>

Call a function when a user changes the 
selected option of a <select> element:
    <select onchange="myFunction()"> 

Call a function when a form is submitted:
    <form onsubmit="myFunction()">
        Enter name: <input type="text">
        <input type="submit">
    </form> 

Call a function when an input field gets focus:
    <input type="text" onfocus="myFunction()"> 
*/

function cambiarImagen() {
	let imagen = document.getElementById('imagen');
	let opcion = document.getElementById('tipo-salon');
	let evento = document.getElementById('evento');
	let checkbox = document.getElementById('evento-adicional');

	switch (opcion.value) {
		case 'chico':
			imagen.src = './salon-chico.jpg';
			evento.style.display = 'none';
			checkbox.checked = false;
			break;
		case 'mediano':
			imagen.src = './salon-mediano.jpg';
			evento.style.display = 'none';
			checkbox.checked = false;
			break;
		case 'grande':
			imagen.src = './salon-grande.jpg';
			evento.style.display = 'block';
			break;
		default:
			imagen.src = 'party.png';
			evento.style.display = 'none';
			checkbox.checked = false;
			break;
	}
}

function validarInvitados() {
	let cantidad = document.getElementById('cantidad-invitados');
	if (cantidad.value < 100 || cantidad.value > 500) {
		cantidad.style.border = '3px solid red';
	} else {
		cantidad.style.border = 'none';
	}
}

function registrar() {
	let registro_nombre = document.getElementById('registro-nombre');
	let registro_invitados = document.getElementById('registro-invitados');
	let registro_valor_final = document.getElementById('registro-valor-total');
	let nombre = document.getElementById('nombre-reserva').value;
	let invitados = document.getElementById('cantidad-invitados').value;
	let tipo_salon = document.getElementById('tipo-salon').value;
	let evento_adicional = document.getElementById('evento-adicional');

	let total;
	switch (tipo_salon) {
		case 'chico':
			total = 500000;
			break;
		case 'mediano':
			total = 700000;
			break;
		case 'grande':
			total = 1000000;
			break;
		default:
			break;
	}
	if (evento_adicional.checked == true) {
		total += total * 0.3;
	}

	registro_nombre.innerHTML = 'La reserva ha sido realizada por ' + nombre;
	registro_invitados.innerHTML = 'La cantidad de invitados son: ' + invitados;
	registro_valor_final.innerHTML = 'El valor total es de: ' + total;
}
