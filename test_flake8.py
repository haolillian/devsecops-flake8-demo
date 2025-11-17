import os, sys   # E401, F401

password = "123456"  # Hardcoded password example

def hello(name):
    eval("print('Hello ' + name)")  # Potential security risk
