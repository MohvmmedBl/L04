import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_valid_password():
    assert is_valid_password("abcdefgh") == False


# bug report 2
def test_r2_clamp_boundary():
    assert clamp(3, 1, 5) == 3


# bug report 3
def test_r3_is_passing():
    assert is_passing(5) == True
