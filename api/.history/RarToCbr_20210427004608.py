import re
import os
import shutil

class ConversorCbr:
    def __init__(self, main_folder):
        self.main_folder = main_folder
    
    def readAndConvertFiles(self):
        for root, dirs, files in os.walk(self.main_folder):
            self.root = root
            self.dirs = dirs
            self.files = files
            self.iterate_files()
            
    def rename_file(self, file):
        try:
            new_file_name = self.rarToCbr(file)
            
            old_file_full_path = os.path.join(self.root, file)
            new_file_full_path = os.path.join(self.root, new_file_name)
            
            print(f'Convertendo arquivo "{file}" para "{new_file_name}')
            shutil.move(old_file_full_path, new_file_full_path)
            
            return True
        except IOError as e:
            print('Erro ao converter arquivo. "%s"' % e)
            return False
            
            
    @staticmethod
    def rarToCbr(file):
        f_name, f_extension = os.path.splitext(file)
        # f_name_numbers = re.findall(r'\d+', f_name)
        
        return f'{f_name}.cbr'
            
    def iterate_files(self):
        for file in self.files:
            if re.search(r'\.rar$', file):
                self.rename_file(file)
        