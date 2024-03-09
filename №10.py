import pytest


phrase = input("Set a phrase: ")

assert len(phrase) < 15, f'Len phrase < 15'

