from gtts import gTTS
from playsound import playsound, PlaysoundException
from inspect    import getsource
from os.path    import abspath, dirname, join
from setuptools import setup

class Voz:

    def __init__(self) -> None:
        here = abspath(dirname(getsource(lambda:0)))
        self.audio = here + '/voz.mp3'
        self.language = 'pt-br'

    def falar_msg(self, msg, language='pt-br'):
        try:
            sp = gTTS(
                text = msg,
                lang = language
            )
            sp.save(self.audio)
            
            playsound(self.audio)            
        except PlaysoundException:
            print(f"Falha ao salvar o arquivo de audio (dir: {self.audio})")

    @property
    def audio(self):
        return self.__audio

    @audio.setter
    def audio(self, nome_arquivo):
        self.__audio = nome_arquivo

