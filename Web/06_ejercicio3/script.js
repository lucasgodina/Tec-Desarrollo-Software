const hamburger = document.querySelector('.hamburger');
const navLink = document.querySelector('.nav__link');

hamburger.addEventListener('click', () => {
	navLink.classList.toggle('hide');
});

const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const campos_deuda = document.querySelectorAll('.campo-deuda');
const montos_deuda = document.querySelectorAll('input[type="number"]');

//Muestra campo deuda para todos los checkboxes
for (let i = 0; checkboxes.length; i++) {
	checkboxes[i].addEventListener('click', () => {
		if (checkboxes[i].checked == true) {
			campos_deuda[i].style.display = 'block';
		} else {
			campos_deuda[i].style.display = 'none';
			montos_deuda[i].value = null;
		}
	});
}

//Funcion para actualizar el innerText de los parrafos .deuda
function actualizarDeuda() {
	const deuda = document.querySelectorAll('.deuda');
	for (let i = 0; i < deuda.length; i++) {
		deuda[i].innerText = `Debe depto ${i + 1}: ${montos_deuda[i].value}`;
	}
}

//Funcion para ocultar los campos de deuda
function ocultarCamposDeuda() {
	const campos_deuda = document.querySelectorAll('.deuda');
	for (let i = 0; i < campos_deuda.length; i++) {
		campos_deuda[i].style.display = 'none';
	}
}

//Funcion para validar el monto de deuda
function validarMontoDeuda(monto = 1000) {
	if (monto < 1000 || monto > 200000) {
		alert('Debe ingresar un monto entre 1000 y 200000');
		return false;
	} else {
		return true;
	}
}

//Funcion para mostrar los despedidos si el monto de deuda es mayor a 180000
function mostrarDespedidos() {
	const despedidos = document.querySelectorAll('.despedido');
	for (let i = 0; i < despedidos.length; i++) {
		if (montos_deuda[i].value > 180000) {
			despedidos[i].style.display = 'block';
		} else {
			despedidos[i].style.display = 'none';
		}
	}
}

//Calcular deuda total
const boton = document.getElementById('calcular');
boton.addEventListener('click', () => {
	const deuda_total = document.getElementById('deuda-total');
	let total = 0;
	for (let i = 0; checkboxes.length; i++) {
		if (checkboxes.checked == true) {
			validarMontoDeuda(montos_deuda[i]);
			montos_deuda;
		}
	}
	montos_deuda.forEach((monto) => {
		total += monto;
	});
	mostrarDespedidos();
	actualizarDeuda();
	ocultarCamposDeuda();
	deuda_total.innerHTML = total;
});
