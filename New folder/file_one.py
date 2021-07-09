# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:29:20 2021

@author: YXG0RZH
"""
import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   file_two.function_three()
else:
   print("File one executed when imported")