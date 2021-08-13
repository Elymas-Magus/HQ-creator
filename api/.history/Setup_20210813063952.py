from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages': ["App", "sys", "Conversor", "Path", "Compressor", "patoolib", "shutil", "os"],
    },    
}

setup(
    name = "HQ - module-creation",
    options = options,
    version = "0.0",
    description = 'Criador de HQ',
    executables = executables
)