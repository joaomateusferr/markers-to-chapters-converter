<?php


    use App\Services\UploadFileParser;
    use \Exception;

    try{

        if(empty($_FILES))
            throw new Exception('Upload issue!');

        $CsvPath = (new UploadFileParser($_FILES))->getPath();


    } catch (Exception $Exception) {

        echo '<h1 class="error">'.$Exception->getMessage().'</h1>';
        exit;

    }

?>