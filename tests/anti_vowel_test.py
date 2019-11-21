import pytest
from pythonExercises import anti_vowel

def testAntiVowelWord():
    assert anti_vowel.anti_vowel("adjfhekoh") == "djfhkh"

def testAntiVowelSentence():
    assert anti_vowel.anti_vowel("Hello, I am a ROBOT") == "Hll,  m  RBT"
