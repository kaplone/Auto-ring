import sys
import os, os.path
import shutil


def pair_up(nombre_a_verifier) :
	nombre_a_verifier = int(nombre_a_verifier)
	if nombre_a_verifier % 2 == 0 :
		return int(nombre_a_verifier)
	else :
		return nombre_a_verifier + 1

def pair_down(nombre_a_verifier) :
	nombre_a_verifier = int(nombre_a_verifier)
	if nombre_a_verifier % 2 == 0 :
		return int(nombre_a_verifier)
	else :
		return nombre_a_verifier - 1
