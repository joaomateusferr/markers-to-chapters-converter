import sys
import getopt
import csv
import os.path
from pathlib import Path

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
                RowTimeArray.pop(3) #remove marker frames
            else:
                RowTimeArray.pop(0) #remove marker hour
                RowTimeArray.pop(2) #remove marker frames

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

def validatePath(FilePath):

    Basename = os.path.dirname(FilePath)

    Dir = Path(Basename)

    if Dir.exists():

        return FilePath
    
    else:

        raise TypeError("Path does not exist!")

    
def validateBooleanResponse(ResponseString):

    if isinstance(ResponseString, (bool)):
        return ResponseString

    if isinstance(ResponseString, (str)):

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
            StringYoutubeChapters = StringYoutubeChapters + "\n"

    StringYoutubeChapters = StringYoutubeChapters[:-1]

    return StringYoutubeChapters

def exportYoutubeChapters(StringYoutubeChapters, ExportFilePath):
    #do it!
    print(str(StringYoutubeChapters))


def validateInputs(FilePath, ExportColor, MoreThanAnHour, ExportFile, ExportFilePath):

    Result = {}
    
    try:
        checkCsvFile(FilePath)
    except Exception as Ex: 
        print("Something went wrong(2) ...\n"+ str(Ex))
        sys.exit(0)

    Result['FilePath'] = FilePath

    try:
        ExportColor = validateBooleanResponse(ExportColor)
    except Exception as Ex: 
        print("Something went wrong(3) ...\n"+ str(Ex))
        sys.exit(0)

    Result['ExportColor'] = ExportColor

    try:
        MoreThanAnHour = validateBooleanResponse(MoreThanAnHour)
    except Exception as Ex: 
        print("Something went wrong(4) ...\n"+ str(Ex))
        sys.exit(0)

    Result['MoreThanAnHour'] = MoreThanAnHour

    try:
        ExportFile = validateBooleanResponse(ExportFile)
    except Exception as Ex: 
        print("Something went wrong(5) ...\n"+ str(Ex))
        sys.exit(0)

    Result['ExportFile'] = ExportFile

    if ExportFile:

        try:
            ExportFilePath = validatePath(ExportFilePath)
        except Exception as Ex: 
            print("Something went wrong(6) ...\n"+ str(Ex))
            sys.exit(0)

        Result['ExportFilePath'] = ExportFilePath

    return Result

def run(FilePath, ExportColor, MoreThanAnHour, ExportFile, ExportFilePath):

    try:
        Result = validateInputs(FilePath, ExportColor, MoreThanAnHour, ExportFile, ExportFilePath)
    except Exception as Ex: 
        print("Something went wrong(7) ...\n"+ str(Ex))
        sys.exit(0)

    try:
        YoutubeChapters = parseCsvFile(Result['FilePath'], Result['MoreThanAnHour'],  Result['ExportColor'])
    except Exception as Ex: 
        print("Something went wrong(8) ...\n"+ str(Ex))
        sys.exit(0)

    if not YoutubeChapters:
        print("Something went wrong(9) ...\nYoutube chapters is empty!")
        sys.exit(0)

    StringYoutubeChapters = stringYoutubeChapters(YoutubeChapters, Result['ExportColor'])

    if ExportFile:

        try:
            exportYoutubeChapters(StringYoutubeChapters, Result['ExportColor'])
        except Exception as Ex: 
            print("Something went wrong(10) ...\n"+ str(Ex))
            sys.exit(0)
                
    else:
        print(StringYoutubeChapters)

def showManual():
    #do it!
    print('Show manual!')

def openGui():
    #do it!
    print('Using gui!')
                
def main():

    #mode 0 use terminal, command line utility or user input
    #mode 1 use gui
    Mode = 0

    OptionsString = 'f:e:mch?'
    FilePath = ExportFilePath = ''
    ExportColor = MoreThanAnHour = ExportFile = False
    YoutubeChapters = []

    if Mode == 0:

        Argv = sys.argv[1:]

        if Argv:    #if contains arguments use command line utility mode

            try:
                Options, Arguments = getopt.getopt(Argv, OptionsString)
            except Exception as Ex: 
                print("Something went wrong(0) ...\n"+ str(Ex))

            for Options, Arguments in Options:
                
                if Options in ['-h', '-?']:
                    showManual()
                    sys.exit(0)
                elif Options in ['-f']:
                    FilePath = Arguments
                elif Options in ['-m']:
                    MoreThanAnHour = True
                elif Options in ['-c']:
                    ExportColor = True
                elif Options in ['-e']:
                    ExportFile = True
                    ExportFilePath = Arguments

        else:   #otherwise requires user input in the terminal

            FilePath = input("Enter the csv path: ")
            ExportColor = input("Do you want to export marker colors if they exist? (y/n) ")
            MoreThanAnHour = input("Is the timeline longer than an hour? (y/n) ")
            ExportFile = input("Do you want to export the chapters as a text file? (y/n) ")

            try:
                ExportFile = validateBooleanResponse(ExportFile)
            except Exception as Ex: 
                print("Something went wrong(1) ...\n"+ str(Ex))
                sys.exit(0)

            if ExportFile:
                ExportFilePath = input("Enter the export path: ")
            else:
                ExportFilePath = ''
    
        
        run(FilePath, ExportColor, MoreThanAnHour, ExportFile, ExportFilePath)

    else:

        openGui()
        

main()