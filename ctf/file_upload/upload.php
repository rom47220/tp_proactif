<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $file = $_FILES['file'];
    $target = __DIR__ . "/uploads/" . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $target)) {
        echo "Upload réussi ! <a href='uploads/".basename($file['name'])."'>Voir le fichier</a>";
    } else {
        echo "Échec de l'upload";
    }
} else {
?>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Uploader</button>
</form>
<?php
}
?>
