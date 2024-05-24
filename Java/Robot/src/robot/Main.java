package robot;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Persona persona = new Persona("Lucas", "Godina");
		Robot robot = new Robot("Sam");
		
		robot.saludar();
		robot.saludar(persona);
	}

}
