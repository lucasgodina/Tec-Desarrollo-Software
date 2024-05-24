package maquina_cafe;

public class MaquinaCafe {
	private int nivelAgua;
	private int cantidadVasos;
	
	public MaquinaCafe(int nivelAgua, int cantidadVasos) {
		this.nivelAgua = nivelAgua;
		this.cantidadVasos = cantidadVasos;
	}
	
	public void prender() {
		System.out.println("Encendiendo maquina..");
	}
	
	public void apagar() {
		System.out.println("Apagando maquina..");
	}
	
	
	
	
	
	
	
}
