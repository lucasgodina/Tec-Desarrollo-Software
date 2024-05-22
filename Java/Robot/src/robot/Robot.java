package robot;

public class Robot {
	private String nombre;

	public Robot(String nombre) {
		this.nombre = nombre;
	}

	public String getNombre() {
		return nombre;
	}

	private void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public void saludar() {
		System.out.println("Hola, mi nombre es " + nombre + ". ¿En que puedo ayudarte?");
	}
	
	public void saludar(Persona persona) {
		System.out.println("Hola " + persona.getNombreCompleto() + ", mi nombre es " + nombre + ". ¿En que puedo ayudarte?");
	}
}
