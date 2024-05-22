package paquete;

public class Fecha {
	private int dia, mes, anio;

	public Fecha(int dia, int mes, int anio) {
		this.dia = dia;
		this.mes = mes;
		this.anio = anio;
	}

	public void mostrarComoCadena() {
		System.out.println(dia + "/" + mes + "/" + anio);
	}
}
