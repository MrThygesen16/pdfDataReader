import PyPDF3

def readPDF(fileIn, pageNum, fileOut):
    # OPEN PDF FIlE
    pdfFileObj = open(fileIn, 'rb')
    pdfReader = PyPDF3.PdfFileReader(pdfFileObj)

    # Select page to read/extract
    pageObj = pdfReader.getPage(pageNum-1)
    
    # extracted text from specified page
    extr = pageObj.extractText()

    # split extracted data by newline char: '\n'
    words = extr.splitlines()

    # Remove leading/trailing spaces for all items
    for x in range(len(words)):
        words[x] = words[x].strip()        

    # We only want the data from the table
    #   starIindex is where we start extracting data 
    #   endIdenx is where we stop extracting data
    startIndex = 0
    endIndex = 0

    # here we find startIndex
    #   essentially with the way this data is formatted
    #   the first purely numeric value we come across will
    #   be the first item in the table
    for x in range(len(words)):
        if words[x].isnumeric():
            startIndex = x
            break

    # here we find endIndex
    #   Similar process as finding the first, but instead
    #   we start from end of the list of words...
    #   Essentially, in all the tables the very last item 
    #   of each will be a decimal value. We want to make sure
    #   that the item we choose has a decimal point, but no spaces...
    for x in range(len(words)-1,0,-1):
        if ("." in words[x] and " " not in words[x] and "$" not in words[x]):
            endIndex = x
            endIndex = endIndex + 1
            break

    # here we slice the list of words
    words = words [startIndex:endIndex]

    #words = words[30:910]

    #print(*words, sep="\n")


    # since we are exporting to a CSV file
    #   (Comma Seperated Values), some of the data
    #   has commas in it to make sense of thousands: e.g. 3,000
    #   we want to get rid of any commas so that it formats correctly
    #   when we open the CSV file in excel
    for x in range(len(words)):
        if "," in words[x]:
            words[x] = words[x].replace(",","")


    newList = []
    tempCol = 0

    # here we are figuring out the # of columns in the table
    #   Essentially we are lucky that the first column 
    #   always contains numbers 15-69 (peoples age)...
    #   So when we come across the first value that's
    #   of length 2 and is less than or equal to 69; 
    #   that's the start of a new column
    for x in range(0,len(words)):
        if x != 0:
            if (len(words[x])== 2 and int(words[x]) <= 69):
                tempCol = x
                break
    
    # here we split the data into an array of arrays
    #   by chunking them by the size of the column we found earlier
    for x in range(0,len(words),tempCol):
        newWord = words[x:x+tempCol]
        newList.append(newWord)

    # we have extracted all the data 
    #   so we can close the pdf reader
    pdfFileObj.close()

    # call our write CSV function
    output = writeCSV(newList, fileOut, tempCol)

    # string for giving user feedback on extraction progress
    output = "\nWrote Contents of Page [" + str(pageNum) + "] to [" + output + "]"

    print(output)


# unused but useful method
def dataToConsole(oldList):
    otherList = []
    
    for item in oldList:
        a = ""

        for newW in item:
            a = a + newW.strip() + " "
        otherList.append(a)

    finalList = []    

    for string in otherList:
        finalList.append(string)
    
    print("\nFormatted Data should appear in specified csv file.\n")
    print(*finalList, sep = "\n")


 


def writeCSV(data, fileName, nmCol):
    newCol = nmCol - 1    # we do -1 here since arrays are index at 0
    with open(fileName, "w") as file:     
        for item in data:
            for x in range(0,len(item)):
                if x == newCol: # if this is true, we have started a new row
                    file.write(item[x] + "\n")
                else:
                    file.write(item[x] + ",")
    f = fileName
    return f




if __name__ == '__main__':

     
    
    for x in range(1,13):
        if (x < 10):
            readPDF("C:/Users/Michael/Documents/Code/pdfDataReader/src/rsig2.pdf", x, "page_0"+str(x)+".csv")
        else:
            readPDF("C:/Users/Michael/Documents/Code/pdfDataReader/src/rsig2.pdf", x, "page_"+str(x)+".csv")
        
        

    print("\nFile Extraction Completed\n")   

#   selected = False
#   while (not selected):
#        try:
#            print("Valid Pages: 1 - 12")
#            choice = int(input("\nEnter Page # to be exported: "))
#
#            if (choice >= 1 and choice <= 12):
#               readPDF("C:/Users/Michael/Documents/Code/Python/rsig2.pdf", choice, "dataResult.csv")
#                selected = True
#
#        except:
#            print("\nINVALID\n")