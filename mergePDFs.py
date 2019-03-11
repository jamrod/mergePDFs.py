#python script to merge pdf files into one document
import PyPDF2
import os

#initialize variables
files = []
start = True
print("Files will be paginated in the order that you add them")

#Ask user for files
def startFiles():
    '''Get files to merge and evaluate if exists
    Returns: Boolean
    '''
    file1 = input("Path to first file:")
    file2 = input("Path to next file:")
    if os.path.isfile(file1) and os.path.isfile(file2):
        files.append(file1)
        files.append(file2)
        return False
    else:
        print("Couldn't find one of the files specified")
        return True

while start:
    start = startFiles()

#check if more files are desired to be merged
needMore = input("need another? 'y/n':")

def getFile(count):
    '''Add additional files to be merged and evaluate if exists
    Keyword arguments:
    count -- number of files in list currently
    Returns: Boolean
    '''
    count = count + 1
    token = input("Path to next file:")
    if os.path.isfile(token):
        files.append(token)
        moreAgain = input("need another? 'y/n':")
        if moreAgain == 'y':
            return True
        else:
            return False
    else:
        print("Couldn't find the file specified, no file added")
        return True

if needMore == "y":
    more = True
else:
    more = False

#Add additional files if needed
while more:
    count = len(files)
    more = getFile(count)

#Get name for output file
newFileName = input("What should we name the new file:")

pdfWriter = PyPDF2.PdfFileWriter()

#loop through PDFs
for filename in files:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    #save PDF to file, wb is write binary
    pdfOutput = open(newFileName+'.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

#Successful output
print("merged", files,  "to", newFileName)
