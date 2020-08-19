from cx_Freeze import setup, Executable 
import os
import sys
options = {"build_exe": {}}
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
if sys.platform == "win32":
    options["build_exe"]['include_files'] = [
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'libcrypto-1_1-x64.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'libssl-1_1-x64.dll'),
     ]
#C:\Users\ykala\AppData\Local\Programs\Python\Python37\tcl
# os.environ['TCL_LIBRARY'] = "C:\\Users\\ykala\\Appdata\\Local\Programs\\Python\\Python37\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Users\\ykala\\Appdata\\Local\Programs\\Python\\Python37\\tk8.6"
  
setup(name = "DrugNN" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("app.py")])
