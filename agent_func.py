

"""
_run_test_id is always passed to all the methods that you create
"""
import datetime
import requests
import subprocess

def give_time():
    """returns the current date"""
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

def give_name():
    """returns the your name"""
    return "Barko Agent 007"
