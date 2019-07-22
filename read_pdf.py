import PyPDF2
from os import chdir, path, getcwd
from pathlib import Path

# get pdf location (for testing it will be in 'desktop\PDF_reader')
working_dir = path.join(Path.home(), r"Desktop\PDF_Reader")


# get PDF to read
pdf_document = "755-33-012_AddressAssignment2019.pdf"

class AddressPoint:
    '''Contains all information extracted from the PDF for easy reference'''

    def __init__(self, file_name, file_path=getcwd(), print_init=True):

        self.full_pdf_path = path.join(file_path, file_name) # get pdf location
        self.raw_text = self.extract_text() # extract all raw text from pdf
        self.clean_text = self.prepare_text() # text striped of most junk
        keyword_dict = self.extract_keywords() # dict with key info

        self.application_type = keyword_dict['appl_type'] # Assign, Change, etc
        self.application_date = keyword_dict['appl_date']
        self.pidnum = keyword_dict['pidnum'] # parcel identification number
        self.full_address = keyword_dict['full_address'] # full adress
        self.st_num = keyword_dict['st_num']
        self.st_name = keyword_dict['st_name']
        self.st_type = keyword_dict['st_type']
        self.zipcode = keyword_dict['zipcode']
        self.esn = keyword_dict['esn']

        if print_init:
            self.print_info()

    def extract_text(self):
        '''Extracts full raw text from the PDF path provided (path/file.pdf)'''

        pdf_file = open(self.full_pdf_path, 'rb')

        # return all of the text from page 0 
        return PyPDF2.PdfFileReader(pdf_file).getPage(0).extractText()

    def prepare_text(self):
        '''Cleans all of the unecessary text possible w/o compromissing data'''

        # remove top and bottom of document with useless info
        clean_text = self.raw_text.split('ADDRESS\n ')[1]
        clean_text = clean_text.split(' New Street Address of Property\n')[0]

        return clean_text

    def extract_keywords(self):
        '''Extracts the AddressPoint Data from the cleaned text; gets date'''
        # returns dictionary -> e.g. keyword_dict['pidnum']

        # APPLICATION TYPE (AREA 1)
        X_index = self.clean_text.index('X') # gets the index of 1st 'X' in doc
        appl_type_txt = self.clean_text[:X_index].split()[-1] # gets the type

        # PIDNUM (AREA 2)
        pidnum_txt = self.clean_text.split('Book \n')[1]
        
        # iterate through pid_nmum text and extract just the 1st 6 integers
        pidnum = self.iter_ndigits(pidnum_txt, 8)

        # FULL ADDRESS, ZIPCODE, EMZ (AREA 3)

    def iter_ndigits(self, text_str, n): # returns the firsts n digits from a text
        '''iterates through a string and retuns only the first n ints'''

        ndigits = ''
        for char in text_str:
            if char.isdigit():
                ndigits += char
            if len(ndigits) == n:
                return ndigits

            # may need to check if string ran out w/o the desired num of digits

    def print_info(self):
        '''print info from self AddressPoint instance'''

        print(f'''\
        APPLICATION TYPE: {self.application_type}
        ADDRESS_NUMBER: {self.st_num}
        STREET_NAME: {self.st_name}
        STREET_TYPE: {self.st_type}
        ZIP_CODE: {self.zipcode}
        FULL_ADDRESS: {self.full_address}
        PARCEL_KEY: {self.pidnum}
        ESN: {self.esn}
        ''')