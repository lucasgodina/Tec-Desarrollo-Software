package paquete;

public class Main {

	public static void main(String[] args) {
		Celular miCelular = new Celular("Samsung");
		System.out.println("Marca: " + miCelular.getMarca());
		System.out.println("Estado: " + miCelular.isEncendido());
		miCelular.prender();
		miCelular.llamar("15-47890643");
		miCelular.apagar();
		miCelular.llamar("15-98067546");
	}
}
