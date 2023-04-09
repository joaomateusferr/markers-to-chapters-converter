import csv
import os.path

def parseCsvFile(CsvPath, MoreThanAnHour, ExportColor):

    YoutubeChapters = []

    with open(CsvPath, mode='r') as CsvFile:
        
        CsvReader = csv.DictReader(CsvFile)

        for CsvRow in CsvReader:

            ChapterRow = {}

            if ExportColor:

                RowColor = CsvRow.get('Color')
                
                if RowColor is None:
                    raise TypeError("Color column not found!")

                ChapterRow['Color'] = RowColor

            RowNote = CsvRow.get('Notes')
                
            if RowNote is None:
                raise TypeError("Notes in column not found!")

            ChapterRow['Notes'] = RowNote

            RowTime = CsvRow.get('Source In')
                
            if RowTime is None:
                raise TypeError("Source in column not found!")

            RowTimeArray = RowTime.split(':')

            if MoreThanAnHour:
                RowTimeArray.pop(3)
            else:
                RowTimeArray.pop(0)
                RowTimeArray.pop(2)

            ChapterRow['Time'] = ':'.join(RowTimeArray)

            YoutubeChapters.append(ChapterRow)

    return YoutubeChapters

def checkCsvFile(CsvPath):

    Exists = os.path.exists(CsvPath)

    if Exists:

        IsFile = os.path.isfile(CsvPath)

        if IsFile:

            FileName, FileExtension = os.path.splitext(CsvPath)

            if FileExtension == '.csv':
                return True
            else:
                raise TypeError("File is not a csv!")

        else:
            raise TypeError("Path does not lead to a file!")

    else:
        raise TypeError("Path does not exist!")
    
                
def main():

    FilePath = 'timeline1.csv'
    ExportColor = False
    MoreThanAnHour = False
    ExportFile = False
    ExportFilePath = ''

    try:

        FileOk = checkCsvFile(FilePath)
    
        if FileOk :
            YoutubeChapters = parseCsvFile(FilePath, MoreThanAnHour, ExportColor)
            #print(str(YoutubeChapters))

    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

main()