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

def validatePath(Path):

    Exists = os.path.exists(Path)

    if Exists:

        IsFile = os.path.isfile(Path)

        if IsFile:

            raise TypeError("Path lead to a file!")
        
        else:

            return True
    
    else:

        raise TypeError("Path does not exist!")

    
def validateBooleanResponse(ResponseString):

    PositiveAnswersAccepted = ['y', 'yes', 'yep']
    NegativeAnswersAccepted = ['n', 'no', 'nop']

    ResponseString = ResponseString.lower()

    if ResponseString in PositiveAnswersAccepted: return True
    if ResponseString in NegativeAnswersAccepted: return False

    raise TypeError("Invalid answer!\nAccepted answers are:\n"+ str(PositiveAnswersAccepted) + "\n" + str(NegativeAnswersAccepted))

def stringYoutubeChapters(YoutubeChapters, ExportColor):

    StringYoutubeChapters = ''

    for Chapter in YoutubeChapters:

        StringYoutubeChapters = StringYoutubeChapters + Chapter['Time'] + " - " + Chapter['Notes'] 

        if ExportColor:
            StringYoutubeChapters = StringYoutubeChapters + " # " + Chapter['Color'] + "\n"
        else:
            StringYoutubeChapters = "\n"

    return StringYoutubeChapters

def exportYoutubeChapters(StringYoutubeChapters):

    print(str(YoutubeChapters))

                
def main():

    FilePath =  ExportFilePath = ''
    ExportColor = MoreThanAnHour = ExportFile = False
    YoutubeChapters = []

    FilePath = input("Enter the csv path: ")
    
    try:
        checkCsvFile(FilePath)
    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

    ExportColor = input("Do you want to export marker colors if they exist? (y/n) ")

    try:
        ExportColor = validateBooleanResponse(ExportColor)
    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

    MoreThanAnHour = input("Is the timeline longer than an hour? (y/n) ")

    try:
        MoreThanAnHour = validateBooleanResponse(MoreThanAnHour)
    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

    ExportFile = input("Do you want to export the chapters as a text file? (y/n) ")

    try:
        ExportFile = validateBooleanResponse(ExportFile)
    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

    if ExportFile:

        ExportFilePath = input("Enter the export path ")

        try:
            ExportFilePath = validatePath(ExportFilePath)
        except Exception as Ex: 
            print("Something went wrong ...\n"+ str(Ex))

    try:
        YoutubeChapters = parseCsvFile(FilePath, MoreThanAnHour, ExportColor)
    except Exception as Ex: 
        print("Something went wrong ...\n"+ str(Ex))

    if not YoutubeChapters:
        print("Something went wrong ...\nYoutube chapters is empty!")

    StringYoutubeChapters = stringYoutubeChapters(YoutubeChapters, ExportColor)

    if ExportFile:        
        exportYoutubeChapters(StringYoutubeChapters, ExportFilePath)
    else:
        print(StringYoutubeChapters)
        

main()