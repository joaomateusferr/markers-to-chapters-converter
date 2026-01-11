<?php



namespace App\Services;

use \Exception;

class UploadFileParser {

    private string $Path;

    public function __construct(array $File) {

        if (!isset($File['csv']) || $File['csv']['error'] !== UPLOAD_ERR_OK)
            throw new Exception('Upload error!');

        $File = $File['csv'];

        if ($File['size'] > 5 * 1024 * 1024)
            throw new Exception('The file exceeds the 5MB limit!');

        if(!in_array($File['type'], ['text/csv']) || pathinfo($File['name'], PATHINFO_EXTENSION) != 'csv')
            throw new Exception('Invalid file type. Please upload a CSV!');

        if(!file_exists($File['tmp_name']))
            throw new Exception('File does not exist!');

        $this->Path = $File['tmp_name'];

    }

    public function getPath() : string {

        return $this->Path;

    }


}