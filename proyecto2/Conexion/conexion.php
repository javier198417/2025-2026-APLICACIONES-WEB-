<?php
// Configuración de la base de datos
$servidor = "localhost";
$usuario = "root";        // Usuario por defecto en XAMPP
$contrasena = "";          // Sin contraseña en XAMPP
$base_datos = "inventario_db";

// Crear conexión
$conn = new mysqli($servidor, $usuario, $contrasena, $base_datos);

// Verificar conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Establecer el juego de caracteres
$conn->set_charset("utf8mb4");

// echo "Conexión exitosa"; // Puedes descomentar para probar
?>