const hamburger = document.querySelector('.hamburger');
const navLink = document.querySelector('.nav__link');

hamburger.addEventListener('click', () => {
	navLink.classList.toggle('hide');
});

function validarMonto() {
	const monto = document.getElementById('monto').value;

	if (monto < 1000000 || monto > 20000000) {
		alert('Debe ingresar un numero entre 1000000 y 20000000');
		return false;
	}
	return true;
}

function cambiarImagen() {
	const cantidad = document.getElementById('cantidad-habitantes');
	const imagen = document.getElementById('imagen');
	switch (cantidad.value) {
		case '1':
			imagen.src = './persona-una.jpg';
			break;
		case '2':
			imagen.src = './persona-dos.jpg';
			break;
		case '3':
			imagen.src = './persona-tres.jpg';
			break;
		case '4':
			imagen.src = './persona-cuatro.jpg';
			break;
		default:
			imagen.src = './casa.jpg';
			break;
	}
}

function esCountry() {
	const monto = document.getElementById('monto').value;
	const tipo_casa = document.getElementById('tipo-casa');
	const country = document.getElementById('country');

	if (monto > 10000000 && tipo_casa.value == 'casa') {
		country.style.display = 'block';
	} else {
		country.style.display = 'none';
		country.checked = false;
	}
}

function calcularCuota() {
	if (validarMonto() == true) {
		const monto = document.getElementById('monto').value;
		const cantidad_cuotas = document.getElementById('cantidad-cuotas').value;
		const valor_cuota = document.getElementById('valor-cuota');
		const country = document.getElementById('check-country');
		const tipo_casa = document.getElementById('tipo-casa');
		const cantidad_habitantes = document.getElementById('cantidad-habitantes');
		const adicional_html = document.getElementById('adicional');
		const descuento_html = document.getElementById('descuento');
		let total = monto / cantidad_cuotas;
		let adicional;
		let descuento;

		if (country.checked == true) {
			total += total * 0.1;
			adicional = total * 0.1;
		}
		if (tipo_casa.value == 'casa' && cantidad_habitantes.value == '4') {
			total -= total * 0.05;
			descuento = total * 0.05;
		}

		valor_cuota.innerHTML = total;
		adicional_html.innerHTML = 'Adicional: ' + adicional;
		descuento_html.innerHTML = 'Descuento: ' + descuento;
	}
}
