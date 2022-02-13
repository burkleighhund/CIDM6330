import os
from datetime import datetime
import sqlite3
import commands

import pytest

import barky
from barky import Option

@pytest.fixture
def option() -> Option:
    name = "List Bookmarks by date"
    command = commands.ListBookmarksCommand()
    prep_call= None
def test_get_option_choice(option):
    choice = "B"
    userInput = option
    assert userInput == choice



def test_get_new_bookmark_info(option):
    choice = "bookmark id"
    userInput = option
    assert userInput == choice

test_get_option_choice("B")
test_get_new_bookmark_info("bookmark id")