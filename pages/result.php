<?php


    use App\Services\UploadFileParser;
    use App\Services\Marker;
    use \Exception;

    try{

        if(empty($_FILES))
            throw new Exception('Upload issue!');

        $CsvPath = (new UploadFileParser($_FILES))->getPath();
        $Marker = new Marker($CsvPath);
        $Chapters = $Marker->getChapters();

        if(!empty($Chapters)){

            ?>

            <div class="row">
                <h1>Result</h1>
            </div>

            <div class="row">

                <spam class="container col-md-8 result">

                    <?php

                        foreach($Chapters as $Time => $Note){

                            echo '<div class="row">'.$Time.' - '.$Note.'</div>';

                        }

                    ?>

                </spam>

            </div">

            <?php

        }

    } catch (Exception $Exception) {

        echo '<div class="row"><h1 class="error">'.$Exception->getMessage().'</h1></div>';

    }

    ?>

    <div class="row">
        <div class="col-md-4">
            <button onclick="window.location.href = window.location.pathname;">Reload</button>
        </div>
    </div>

    <?php

?>