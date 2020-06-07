from functions import *

def test_vowel_checker():

    assert callable(vowel_checker)
    assert isinstance(vowel_checker('hello'), bool)
    assert vowel_checker('hello') == False

test_vowel_checker()


def test_add_vowel_suffix():

    assert callable(add_vowel_suffix)
    assert isinstance(add_vowel_suffix('are'), str)
    assert add_vowel_suffix('are') == 'are-way'

test_add_vowel_suffix()


def test_remove_vowel_suffix():

    assert callable(remove_vowel_suffix)
    assert isinstance(remove_vowel_suffix('are-way'), str)
    assert remove_vowel_suffix('are-way') == 'are'

test_remove_vowel_suffix()


def test_add_suffix():

    assert callable(add_suffix)
    assert isinstance(add_suffix('hello'), str)
    assert add_suffix('hello') == 'hello-hay'

test_add_suffix()


def test_remove_first_letter():
    assert callable(remove_first_letter)
    assert isinstance(remove_first_letter('hello'), str)
    assert remove_first_letter('hello') == 'ello'

test_remove_first_letter()


def test_add_first_letter():
    assert callable(add_first_letter)
    assert isinstance(add_first_letter('ello-hay'), str)
    assert add_first_letter('ello-hay') == 'hello-hay'

test_add_first_letter()

def test_remove_suffix():
    assert callable(remove_suffix)
    assert isinstance(remove_suffix('hello-hay'), str)
    assert remove_suffix('hello-hay') == 'hello'

test_remove_suffix()

def test_pig_latin_encoder():
    pig_latin_encoder('hello')
    assert callable(pig_latin_encoder)
    assert isinstance(pig_latin_encoder('hello class'), str)
    assert pig_latin_encoder('hello') == 'ello-hay'
    assert pig_latin_encoder('apple') == 'apple-way'
    assert pig_latin_encoder('demon') == 'emon-day'
    assert pig_latin_encoder('hoping this code works correctly') ==  'oping-hay his-tay ode-cay orks-way orrectly-cay'


test_pig_latin_encoder()  


def test_pig_latin_decoder():
    assert callable(pig_latin_decoder)
    assert isinstance(pig_latin_decoder('ello-hay'), str)
    assert pig_latin_decoder('ello-hay') == 'hello'
    assert pig_latin_decoder('apple-way') == 'apple'
    assert pig_latin_decoder('emon-day') == 'demon'
    assert pig_latin_decoder('oping-hay his-tay ode-cay orks-way orrectly-cay') == 'hoping this code works correctly'

test_pig_latin_decoder()
