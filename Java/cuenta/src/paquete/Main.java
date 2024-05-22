package paquete;

public class Main {

	public static void main(String[] args) {
		Cuenta miCuenta = new Cuenta(30000.0);
		miCuenta.depositar(20000.0);
		miCuenta.extraer(350.0);
		System.out.println("El saldo de la cuenta es de: " + miCuenta.obtenerSaldo());
	}

}
