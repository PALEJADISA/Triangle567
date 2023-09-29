# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import datetime

# my brand function 
date = datetime.datetime.now()

def my_brand(assigmentName):
  print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")
  


from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    my_brand("HW 01: Testing a legacy program and reporting on testing results")
    # define multiple sets of tests as functions with names that begin
    def test_classify_triangle_validInputs(self): #test Equilateral should pass 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
        
    def test_classify_triangle_validInputsI(self): #test isosceles should pass 
        self.assertEqual(classifyTriangle(1,2,2),'isosceles')
    
    def test_classify_triangle_validInputsII(self): #test right should pass 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def test_classify_triangle_validInputsIII(self): #test scalene should pass 
        self.assertEqual(classifyTriangle(1,2,3),'scalene')

    def test_classify_triangle_invalidInputsStrings(self): #test invalid inputs should no  pass
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput')

    def test_classify_triangle_invalidInputsNegative(self):
        self.assertEqual(classifyTriangle(-1,-2,-3),'InvalidInput')

    def test_classify_triangle_invalidInputsZero(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')

    def test_classify_triangle_invalidInputFloats(self):
        self.assertEqual(classifyTriangle(1.1,1.1,1.1),'InvalidInput')

    def test_classify_triangle_invalidInputsNull(self):
        self.assertEqual(classifyTriangle(None,None,None),'InvalidInput')

    def test_classify_triangle_invalidInputsmissingInputs(self):
        self.assertEqual(classifyTriangle(1,1,),'InvalidInput')

    def test_classify_triangle_invalidInputsGreaterThan200(self):
        self.assertEqual(classifyTriangle(201,300,400),'InvalidInput')
   
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

