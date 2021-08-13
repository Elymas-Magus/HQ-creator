from cx_Freeze import setup, Executable

base = None    

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages': ["App", "sys", "Conversor", "Path", "Compressor", "patoolib", "shutil", "os"],
    },    
}

setup(
    name = "HQ - module-creation",
    options = options,
    version = "0,0",
    description = '<any description>',
    executables = executables
)