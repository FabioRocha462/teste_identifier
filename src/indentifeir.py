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

			

def identificar(string):
	if  (size(string) == True) and (caracter_Special(string,caracter(string))== True) and (first_caracter(string) == True):
		return True
	else:
		return False

	
	