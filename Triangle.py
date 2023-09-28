# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
"""**********************************************************
@modified by Paula A Diaz Silva
**********************************************************"""

import datetime

# my brand function 
date = datetime.datetime.now()
assignmentName = "HW 01: Testing a legacy program and reporting on testing results Part 2"
def my_brand(assigmentName):
  print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
     # verify that all 3 inputs are integers
    if a == None or b == None or c == None:
        raise ValueError("Invalid input.")
    # verify that all 3 inputs are integers
    if a == '' or b == '' or c == '':
        raise ValueError("Invalid input.")
    # verify that all 3 inputs are integers
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    # the sum of any two sides must be strictly less than the third side
    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Invalid side lengths.")
    # verify that all 3 inputs are integers
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        raise ValueError("Invalid input.")
    # greater than 200
    if a > 200 or b > 200 or c > 200:
        raise ValueError("Invalid input.")
   
    #if a is None or b is None or c is None:
        #raise ValueError("Side lengths cannot be None")

    #IF ALL IS GOOD****************
    elif a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    ############elif ((a * 2) + (b * 2)) == (c * 2):  #hipotenuza
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right Triangle'
    else:
        return "Scalene Triangle"



my_brand(assignmentName)
triangle_type = classifyTriangle(3,4,5);
print("Triangle type:", triangle_type)

# end of modfied code
















#*********************code mofified ***************************
    # require that the input values be >= 0 and <= 200
    #if a > 200 or b > 200 or c > 200:
        #return 'InvalidInput'
        
    #if a <= 0 or b <= b or c <= 0:
        #return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    #if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        #return 'InvalidInput'
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    #if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        #return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    #if a == b and b == a:
        #return 'Equilateral'
    #elif ((a * 2) + (b * 2)) == (c * 2):
        #return 'Right'
    #elif (a != b) and  (b != c) and (a != b):
        #return 'Scalene'
    #else:
        #return 'Isoceles'
