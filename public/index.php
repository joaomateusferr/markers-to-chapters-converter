<?php


if(empty($_POST)){

}


?>
<!DOCTYPE html>

<html lang="en-US">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markers Converter</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="box">

    <?php
        if(empty($_FILES)){
            include_once(dirname(__DIR__, 1).'/pages/upload.php');
        } else {
            include_once(dirname(__DIR__, 1).'/pages/result.php');
        }
    ?>

    </div>

</body>
</html>