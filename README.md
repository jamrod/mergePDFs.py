# mergePDFs.py
Merge two or more PDF documents from the terminal with a Python script
--------------------
I made this project because I wanted to be able to quickly merge two PDF documents and could't find a nice way to do it.

Here's what I wanted it to do-

* Prompt me to input my files
* Add more files than 2 if necessary
* Confirm files exist before merging without crashing
* Merge my files in order into a new pdf file
* Give me a success message with the files that I added and the output file listed

This is what I've come up with-

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


After a few tweaks I had this guy working to my liking.

The last thing I wanted to do was make it so I could start the script easily from inside the folder that held my pdfs so I wouldn't have to type long path names for my file locations. I use a Linux distro (mint currently) as my home computer, so I decided I'd make an alias to run my new program. 

To create the alias type-

    nano ~/.bashrc

Then scroll down below where it says "#Alias definitions" and add this-

    alias mergePDFs='python3 /home/james/python/mergePDFs.py"


Of course you'll want to put the actual path to your python script here and adjust the names as you like. Now I can type mergePDFs from any folder in the terminal and start my script. This isn't the only way to add alias's or even the only way to accomplish this goal but it achieved my needs.

Also, credit to [geektechstuff.com](https://geektechstuff.com/2018/02/17/python-3-merge-multiple-pdfs-into-one-pdf/) who I copied a snippet from to use PyPDF2

Thanks for reading, hope this helps someone out there!
