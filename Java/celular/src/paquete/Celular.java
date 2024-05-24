package paquete;

public class Celular {
	private String marca;
	private boolean encendido;

	public Celular(String marca) {
		this.marca = marca;
		encendido = false;
	}
	
	public String getMarca() {
		return marca;
	}
	
	public boolean isEncendido() {
		return encendido;
	}

	public void prender() {
		if (!isEncendido()) {
			encendido = true;
			System.out.println("Encendiendo el celular..");
		}
	}

	public void apagar() {
		if (isEncendido()) {
			encendido = false;
			System.out.println("Apagando el celular..");
		}
	}
	
	public void llamar(String numero) {
		if(isEncendido()) {
			System.out.println("Llamando al numero: " + numero);
		}
	}
}
