# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:32:02 2021

@author: YXG0RZH
"""


print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")