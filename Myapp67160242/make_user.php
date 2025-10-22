<?php
require __DIR__ . '/config_mysqli.php';

$email = '67160242@go.buu.ac.th';
$name  = 'Unnop';
$plain = 'Unnop_090010'; // เปลี่ยนตามต้องการ

$hash = password_hash($plain, PASSWORD_DEFAULT);

$stmt = $mysqli->prepare('INSERT INTO users (email, display_name, password_hash) VALUES (?, ?, ?)');
$stmt->bind_param('sss', $email, $name, $hash);
$stmt->execute();
$stmt->close();

echo "Created user: $email with password: $plain\n";
