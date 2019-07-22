import PyPDF2, sys
from os import chdir, path, getcwd
from pathlib import Path

# get pdf location (for testing it will be in 'desktop\PDF_reader')
working_dir = path.join(Path.home(), r"Desktop\PDF_Reader")

# get PDF to read
pdf_doc = "755-33-012_AddressAssignment2019.pdf"

class AddressPoint:
    '''Contains all information extracted from the PDF for easy reference'''

    def __init__(self, file_name, file_path=getcwd()):

        self.full_pdf_path = path.join(file_path, file_name)
        self.raw_text = self.extract_text()
        self.purified_text = self.clean_text()
        keyword_dict = self.extract_keywords()
        # TODO: RUN METHOD(S) TO EXTRACT TEXT, CLEAN TEXT AND EXTRACT KEYWORDS

        self.pidnum = ''
        self.f_address = '' # full adress
        self.st_num = ''
        self.st_name = ''
        self.st_type = ''
        self.zipcode = ''
        self.esn = ''

    def extract_text(self):
        '''Extracts full raw text from the PDF path provided (path/file.pdf)'''
        pass

    def clean_text(self):
        '''Cleans all of the unecessary text possible w/o compromissing data'''
        pass

    def extract_keywords(self, clean_text):
        '''Extracts the AddressPoint Data from the cleaned text'''
        # returns dictionary keyword_dict['pidnum']
        pass

    def print_info(self):
        '''print relevant info from self AddressPoint instance'''

        print(f'''\
        ADDRESS_NUMBER: {self.st_num}
        STREET_NAME: {self.st_name}
        STREET_TYPE: {self.st_type}
        ZIP_CODE: {self.zipcode}
        FULL_ADDRESS: {self.f_address}
        PARCEL_KEY: {self.pidnum}
        ESN: {self.esn}
        ''')