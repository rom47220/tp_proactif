<?php
$db = new SQLite3('db.sqlite');
$db->exec('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, secret TEXT)');
$db->exec("INSERT OR IGNORE INTO users (id, username, secret) VALUES (1, 'admin', 'FLAG{sql_injection_done}')");

$user = $_GET['user'] ?? '';
$query = "SELECT secret FROM users WHERE username = '$user'";
$result = $db->query($query);

if ($row = $result->fetchArray()) {
    echo "Secret : " . $row['secret'];
} else {
    echo "Il n'y a rien à voir ici, la base de données est probablement inaccessible mon cher $user";
}
?>
