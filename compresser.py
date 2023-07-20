import zipfile
import csv

# create  a compresser class
class Compresser:
    
    # initialize the instance with path of the file you wnat to comress, and where you want it compressed
    # the full file pathe should be inputed if it is not in your current working directory
    def __init__(self, file_path, comp_path): 
        self.file = file_path
        comp_path+='.zip'
        self.comp_path = comp_path
    
    # method  for compressing
    def compress(self):
        zip_file = zipfile.ZipFile(self.comp_path, 'w') # create an Zipfile object
        zip_file.write(self.file, compress_type = zipfile.ZIP_DEFLATED)
        zip_file.close()
        print('File successfully compressed')

    # method for reading the csv file  
    def read_file(self):
        csv_file = open(self.file, encoding = 'utf-8')
        csv_reader = csv.reader(csv_file)
        csv_data = list[csv_reader]
        print(csv_data)



