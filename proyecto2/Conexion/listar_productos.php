<?php
require_once 'conexion.php';

$sql = "SELECT id, nombre, precio, cantidad, fecha_creacion FROM productos";
$resultado = $conn->query($sql);

if ($resultado->num_rows > 0) {
    echo "<h2>Productos en Inventario</h2>";
    echo "<table border='1' cellpadding='8'>";
    echo "<tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Fecha Registro</th>
          </tr>";
    
    while($fila = $resultado->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $fila["id"] . "</td>";
        echo "<td>" . htmlspecialchars($fila["nombre"]) . "</td>";
        echo "<td>$" . number_format($fila["precio"], 2) . "</td>";
        echo "<td>" . $fila["cantidad"] . "</td>";
        echo "<td>" . $fila["fecha_creacion"] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} else {
    echo "No hay productos registrados.";
}

$conn->close();
?>