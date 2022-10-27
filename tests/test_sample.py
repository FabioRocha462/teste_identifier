from src.indentifeir import *


def test_identifier_test_limit_caracter():
    assert identificar("aaaaaa") == True

def test_identifier_test_limit_maiusculas():
    assert identificar("AAAAAA") == True

def test_identifier_test_letras_numeros():
    assert identificar("aabb11") == True

def test_identifier_test_letras_unico_caracter():
    assert identificar("a") == True

def test_identifier_test_letras_acima_do_valor_limite():
    assert identificar("aaadfbbe") == False

def test_identifier_test_inicio_numero():
    assert identificar("1eiei") == False

def test_identifier_test_caracter_especial():
    assert identificar("fjdjd&") == False

def test_identifier_test_vazio():
    assert identificar("") == False

def test_identifier_test_espaco():
    assert identificar(" ") == False