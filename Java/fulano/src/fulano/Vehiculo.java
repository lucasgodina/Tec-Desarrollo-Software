package fulano;

public class Vehiculo {
	private String marca;
	private String modelo;
	private String color;
	private int velocidadMaxima;
	
	public Vehiculo(String marca, String modelo, String color, int velocidadMaxima) {
		super();
		this.marca = marca;
		this.modelo = modelo;
		this.color = color;
		this.velocidadMaxima = velocidadMaxima;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}
	
	
}
