from ctypes import cdll
lib = cdll.LoadLibrary('./libchess.so')
lib.play_chess()
