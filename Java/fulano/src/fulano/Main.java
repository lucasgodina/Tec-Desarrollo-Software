package fulano;

public class Main {

	public static void main(String[] args) {
		Vehiculo vehiculo = new Vehiculo("Giat", "Halio", "gris", 180);
		Propietario propietario = new Propietario("Fulano Gomez", vehiculo);
		
		Vehiculo vehiculo2 = new Vehiculo("Lamborghini", "Murcielago", "Amarillo", 400);
		Propietario propietario2 = new Propietario("Lucas Godina", vehiculo2);
	}
}
