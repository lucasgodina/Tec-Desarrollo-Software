package paquete;

public class Cuenta {
	private double saldo;

	public Cuenta() {

	}

	public Cuenta(double saldo) {
		this.saldo = saldo;
	}

	public void depositar(double importe) {
		saldo += importe;
	}

	public void extraer(double importe) {
		saldo -= importe;
	}

	public double obtenerSaldo() {
		return saldo;
	}
}
