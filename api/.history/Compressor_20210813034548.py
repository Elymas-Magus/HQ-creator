import patoolib

class Compressor:
    def __init__(self):
        patoolib.create_archive("teste.rar", tuple(os.listdir('.')))