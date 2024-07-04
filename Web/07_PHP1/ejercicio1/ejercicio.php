<?php
// Obtener los dos valores introducidos por el usuario
$valor1 = $_POST['valor1'];
$valor2 = $_POST['valor2'];

// Realizar la operacion usando isset
if (isset($_POST['+'])) {
    echo 'La suma es: ' . ($valor1 + $valor2);
}
if (isset($_POST['-'])) {
    echo 'La resta es: ' . ($valor1 - $valor2);
}
if (isset($_POST['*'])) {
    echo 'La multiplicacion es: ' . ($valor1 * $valor2);
}
if (isset($_POST['/'])) {
    echo 'La division es: ' . ($valor1 / $valor2);
}
?>