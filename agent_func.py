

"""
_run_test_id is always passed to all the methods that you create
"""
import datetime
import requests
import subprocess

def give_time(_run_test_id='1') -> str:
    """returns the current date"""
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

def give_name(_run_test_id='1'):
    """returns the your name"""
    return "Barko Agent 007"
