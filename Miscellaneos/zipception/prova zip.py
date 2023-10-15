import zipfile

def extract_zip_files(zip_file):
     with zipfile.ZipFile(zip_file, 'r') as zip_ref:
         zip_ref.extractall()
         while True:
             for file in zip_ref.namelist():
                 if file.endswith('.zip'):
                      extract_zip_files(file)
                 else:
                     break

zip_file = input("Inserisci il nome del file zip da estrarre: ")
extract_zip_files(zip_file)
