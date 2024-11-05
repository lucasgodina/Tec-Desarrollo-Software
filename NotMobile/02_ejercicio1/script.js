function validarDescripcion() {
	let descripcion = document.getElementById("descripcion").value;
	if (
		descripcion != "cama" &&
		descripcion != "mesa" &&
		descripcion != "silla" &&
		descripcion != "ropero"
	) {
		alert("Descripcion incorrecta");
		return false;
	}
	return true;
}

function validarCantidadSolicitada() {
	let cantidad = document.getElementById("cantidad").value;
	if (cantidad < 0 || cantidad > 100) {
		alert("Cantidad incorrecta");
		return false;
	}
	return true;
}

function calcularTotal() {
	if (validarDescripcion() && validarCantidadSolicitada()) {
		let descripcion = document.getElementById("descripcion").value;
		let cantidad = document.getElementById("cantidad").value;
		let tipo;
		let total = 0;

		switch (descripcion) {
			case "mesa":
				tipo = 200000;
				break;
			case "cama":
				tipo = 240000;
				break;
			case "silla":
				tipo = 10000;
				break;
			case "ropero":
				tipo = 350000;
		}

		total = cantidad * tipo;

		if (document.getElementById("envio").checked) {
			total += 2000;
		}

		if (
			document.getElementById("material").value == "algarrobo" &&
			cantidad >= 50
		) {
			total *= 0.9;
		}

		document.getElementById("precio-final").innerHTML = total;
	}
}
