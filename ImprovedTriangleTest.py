import unittest
import datetime

# my brand function 
date = datetime.datetime.now()
assignmentName = "HW 01: Testing a legacy program and reporting on testing results Part 2"
def my_brand(assigmentName):
  print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")
  
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangleType(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral Triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 4), "Isosceles Triangle")

    def test_scalene_triangle(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene Triangle")

    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right Triangle")

    def test_invalid_side_length(self):
        with self.assertRaises(ValueError):
            classifyTriangle(0, 2, 3)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            classifyTriangle(1, 2, 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            classifyTriangle(1, 2, 3.0)

    def test_invalid_input2(self):
        with self.assertRaises(ValueError):
            classifyTriangle(1, 2, 201) 

    def test_invalid_input3(self):
        with self.assertRaises(ValueError):
           classifyTriangle(1, 2, -1)

    def test_invalid_input4(self):
        with self.assertRaises(ValueError):
            classifyTriangle('','','')
    
    def test_invalid_input5(self):
        with self.assertRaises(ValueError):
            classifyTriangle(None, None, None)

    def test_invalid_input6(self):
        with self.assertRaises(ValueError):
            classifyTriangle(0, 0, 0)

if __name__ == "__main__":
    my_brand(assignmentName)
    unittest.main()
    