<?php
require_once 'conexion.php';

// Obtener datos del formulario
$nombre = $_POST['nombre'] ?? '';
$descripcion = $_POST['descripcion'] ?? '';
$precio = $_POST['precio'] ?? 0;
$cantidad = $_POST['cantidad'] ?? 0;

// Validar datos básicos
if (empty($nombre) || $precio <= 0 || $cantidad < 0) {
    die("Error: Datos inválidos");
}

// Usar prepared statement para seguridad (evita SQL injection) [citation:3]
$stmt = $conn->prepare("INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssdi", $nombre, $descripcion, $precio, $cantidad); // s=string, d=double, i=integer

if ($stmt->execute()) {
    echo "✅ Producto guardado correctamente. <a href='listar_productos.php'>Ver productos</a>";
} else {
    echo "❌ Error al guardar: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>