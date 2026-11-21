import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    assert check_admin("") == False


# bug report 2
def test_r2_find_user_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('alice', 'secret')")
    db.commit()
    assert find_user(db, "'; DROP TABLE users; --") is None
