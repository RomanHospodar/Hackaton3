import subprocess
from pathlib import Path
import os

def unzip_model():

    folder_path=Path("Model/MyModel/variables/zip/")
    folder_path2=Path("Model/MyModel/variables/")
    unzip_command = '"C:\\Program Files\\WinRAR\\WinRAR.exe"' + ' e ' + '"' + folder_path.absolute().as_posix() + '"'
    my_file = "Model/MyModel/variables/variables.data-00000-of-00001"
    unzipper = "C:/Program Files/7-Zip/7z.exe"
    winrar = "C:/Program Files/c/WinRAR.exe"
    if not os.path.isfile(my_file):
        # file does not exist
        if not os.path.isfile(winrar):
            # winrar does not exist
            if not os.path.isfile(unzipper):
                # 7-Zip does not exist
                print("Cannot locate unzip tools C:/Program Files/WinRAR/WinRAR.exe or C:/Program Files/7-Zip/7z.exe...")
                exit()
            else:
                # 7-Zip exists
                unzip_command = '"C:\\Program Files\\7-Zip\\7z.exe"' +  ' e ' + '"' + folder_path.absolute().as_posix() + '"'
        print("Unzipping file...")
        subprocess.run(unzip_command, shell=True, cwd=folder_path2)
    else:
        # file exists
        print("Model already exists...")
