<?php


    use App\Services\UploadFileParser;
    use App\Services\Marker;
    use \Exception;

    try{

        if(empty($_FILES))
            throw new Exception('Upload issue!');

        $CsvPath = (new UploadFileParser($_FILES))->getPath();
        $MoreThanAnHour = empty($_POST['hour-plus']) ? false : true;
        $Marker = new Marker($CsvPath, $MoreThanAnHour);
        $Chapters = $Marker->getChapters();

        if(!empty($Chapters)){

            echo '<h1>Result</h1><spam class="result">';

            foreach($Chapters as $Time => $Note){

                echo $Time.' - '.$Note.'<br>';

            }

            echo '</spam>';

        }

    } catch (Exception $Exception) {

        echo '<h1 class="error">'.$Exception->getMessage().'</h1>';
        exit;

    }

?>