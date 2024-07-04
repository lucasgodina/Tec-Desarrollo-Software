<?php
include ("formulario.html");

// Obtener variables nombre y cargo
$nombre = $_POST['nombre'];
$cargo = $_POST['cargo'];

// Si el cargo es cadete, mostrar el nombre, el cargo y que gana 20000
if ($cargo == 'cadete') {
    echo 'El nombre es ' . $nombre . ', el cargo es ' . $cargo . ' y gana 20000';
}