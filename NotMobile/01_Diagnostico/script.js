function calcularEntradas() {
	var cantidad_entradas = document.getElementById("cantidad-entradas").value;
	var tipo_entrada = document.getElementById("tipo-entradas").value;
	var precio_final = cantidad_entradas * tipo_entrada;
	if (document.getElementById("meetup-opt").checked == true) {
		precio_final = precio_final + cantidad_entradas * 75000;
	}
	document.getElementById("precio-final").innerHTML = precio_final;
}
