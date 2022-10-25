from operator import truediv
import re

def size(string):
	if(len(string)>0 and len(string) <=6 ):
		return True
	return False
	
def caracter(string):
	r = re.compile(r'[a-zA-Z]|[0-9]')
	list = re.findall(r,string)
	return list
	
def caracter_Special(string,list):
	if(len(string) == len(list)):
		return True
	return False
	
def first_caracter(string):
	if len(string)  > 0:
		caracter = string[0]
		r = re.compile(r'[a-zA-Z]')
		regex = re.findall(r,caracter)
		if len(regex) >0:
			return True
		return False
	return False

			

def identifeir(string):
	global caracter 
	list = []
	if size == True:
		list.append(1)
	caracter = caracter(string)
	special = caracter_Special(string,caracter)
	if special == True:
		list.append(1)
	fc = first_caracter(string)
	if fc == True:
		list.append(1)

	if len(list) == 3:
		return "válido"
	else:
		return "inválido"
	
	