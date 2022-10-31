import pytest
import os
import sys

noodlemaps_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(noodlemaps_folder)
from src import exp_api_work

def test_says_something():
    response = exp_api_work.say_something()
    assert response == "something"

    