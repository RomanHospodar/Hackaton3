import subprocess
from pathlib import Path
import os

def unzip_model():

    folder_path=Path("Model/MyModel/variables/zip/")
    folder_path2=Path("Model/MyModel/variables/")

    my_file = "Model/MyModel/variables/variables.data-00000-of-00001"
    unzipper = "C:/Program Files/7-Zip/7z.exe"
    if os.path.isfile(unzipper):
        if not os.path.isfile(my_file):
            # file does not exist
            print("Unzipping file...")

            unzip_command = '"C:\\Program Files\\7-Zip\\7z.exe"' +  ' e ' + '"' + folder_path.absolute().as_posix() + '"'
            subprocess.run(unzip_command, shell = True, cwd = folder_path2)
        else:
            print("Model already exists...")
    else:
        print("Cannot locate C:/Program Files/7-Zip/7z.exe...")
        exit

