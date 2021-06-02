# pdfDataReader
Python Script for extracting data from numerous pages in a PDF document. 


### Requirements:

* Python 3
* PyPDF3

### Usage

1. Place the PDF file you want extracted into the folder `pdfs`
2. Run the script and enter the name of PDF file when prompted
3. The output of this script will be placed in the `output` folder


For Example, the PDF file `rsig2.pdf`, that's already in the `pdfs` folder:


    Enter pdf file to read from: rsig2.pdf

    Wrote Contents of Page [1] to [c:\Users\Michael\Documents\Code\pdfDataReader\output/page_01.csv]

    Wrote Contents of Page [2] to [c:\Users\Michael\Documents\Code\pdfDataReader\output/page_02.csv]

    ...       ...       ...       ...       ...       ...       ...       ...       ...       ...
    
    Wrote Contents of Page [11] to [c:\Users\Michael\Documents\Code\pdfDataReader\output/page_11.csv]

    Wrote Contents of Page [12] to [c:\Users\Michael\Documents\Code\pdfDataReader\output/page_12.csv]

    File Extraction Completed
    
 Now when we check the contents of `output`:
 
     page_01.csv
     page_02.csv
     ...
     page11.csv
     page12.csv
  
