import cx_Freeze
from cx_Freeze import *
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\ykala\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\ykala\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

setup(
	name='app',
	options = {'build.exe':{'packages': ['pandas','numpy', 'bioservices']}},
	executables=[
		Executable(
			"app.py",
			)
		]
	)