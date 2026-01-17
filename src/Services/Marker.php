<?php

namespace App\Services;

use \Exception;

class Marker {

    private array $Chapters = [];

    public function __construct(string $CsvPath, bool $MoreThanAnHour) {

        try{

            $Handle = fopen($CsvPath, "r");

            if ($Handle === FALSE)
                throw new Exception("The csv file could not be opened.");

            $Headers = fgetcsv($Handle);

            $Fields = array_flip($Headers);

            if(!isset($Fields['Notes']))
                throw new Exception("Notes column not found!");

            if(!isset($Fields['Source In']))
                throw new Exception("Source in column not found!");

            unset($Fields);

            while (($Row = fgetcsv($Handle)) !== FALSE) {

                $Line = array_combine($Headers, $Row);
                $Content = [];

                foreach($Line as $Key => $Value){

                    if($Key == 'Notes' || $Key == 'Source In'){

                        if($Key == 'Source In'){

                            $Tokens = explode(':', $Value);
                            unset($Tokens[array_key_last($Tokens)]);

                            if(!$MoreThanAnHour)
                                unset($Tokens[0]);

                            $Value = implode(':', $Tokens);

                        }

                        $Content[$Key] = $Value;

                    }

                }

                $Data[] = $Content;

            }

            $Chapters = [];

            foreach($Data as $Line){

                $Chapters[$Line['Source In']] = $Line['Notes'];

            }

            $this->Chapters = $Chapters;

        } catch (Exception $Exception) {

            throw new Exception($Exception->getMessage());

        } finally {

            fclose($Handle);

        }

    }

    public function getChapters() : array {

        return $this->Chapters;

    }

}