<?php

require dirname(__DIR__, 1). '/vendor/autoload.php';

?>

<!DOCTYPE html>

<html lang="en-US">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markers Converter</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

<body>

    <div class="container text-center">

        <?php

            if(empty($_FILES))
                include_once(dirname(__DIR__, 1).'/pages/upload.php');
            else
                include_once(dirname(__DIR__, 1).'/pages/result.php');

        ?>

    </div>

</body>
</html>