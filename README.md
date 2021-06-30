# pdfDataReader
Python script for extracting tables of data from numerous pages in a PDF document. 

*Note: script is still WIP* 

### Requirements:

* Python 3

* PyPDF3

  

### Installation

If python is not already installed use:

```sudo apt install python3.9```

Next to install PyPDF3 we need to install `python3-pip`:

```sudo apt install python3-pip```

Once that has been installed we can install PyPDF3:

```pip install PyPDF3```




### Usage

1. Place the PDF file you want extracted into the folder `pdfs`
2. Run the script and enter the name of PDF file when prompted
3. The output of this script will be placed in the `output` folder
    * Note: the contents of the folder `output` is deleted everytime the script is run


For Example, the PDF file `rsig2.pdf`, that's already in the `pdfs` folder:


    Enter pdf file to read from: rsig2.pdf
    
    Wrote Contents of Page [1] to [c:\Users\Michael\Documents\Code\pdfDataReader\output\page_01.csv]
    
    Wrote Contents of Page [2] to [c:\Users\Michael\Documents\Code\pdfDataReader\output\page_02.csv]
    
    ...       ...       ...       ...       ...       ...       ...       ...       ...       ...
    
    Wrote Contents of Page [11] to [c:\Users\Michael\Documents\Code\pdfDataReader\output\page_11.csv]
    
    Wrote Contents of Page [12] to [c:\Users\Michael\Documents\Code\pdfDataReader\output\page_12.csv]
    
    File Extraction Completed

 Now when we check the contents of the folder `output`:

     page_01.csv
     page_02.csv
     ...
     page11.csv
     page12.csv

  


  N.B. The way this works in 'recognising' the tables is that it uses a start and an end index. 
  Essentially we must find a rule that can satisify the beginning of a new column/row - which is figured out after the table has been recognised...

  A little bit of tweaking to the script must be done so that a specific PDF file will work and produce an ideal output.
