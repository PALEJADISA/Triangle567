import unittest
import datetime

#my brand function 
date = datetime.datetime.now()
assignmentName = "HW 06: Mutation Testing"
def my_brand(assigmentName):
  print(" =*=*=*= Paula A. Diaz Silva  =*=*=*= \n =*=*=*= Course 2023S-SSW567-WS =*=*=*= \n   =*=*=*= " +  assigmentName + " =*=*=*= \n =*=*=*= " + date.strftime("%c") + " =*=*=*=  ")
#classify_triangle
from tri_angle2 import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangleType(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")
    
    #ADDED
    def test_equilateral_triangle_classification(self):
    # In an equilateral triangle, all sides are equal.
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle", "3, 3, 3 is an equilateral triangle.")

        
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 4), "Isosceles Triangle")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene Triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle") #this can be a scalene..
    #ADDED
    def test_scalene_triangle2(self):
        self.assertEqual(classify_triangle(200, 200, 200), "Equilateral Triangle")
        
    #ADDED
    def test_scalene_triangle2(self):
        self.assertEqual(classify_triangle(199, 199, 199), "Equilateral Triangle")

    
    def test_invalid_side_length(self):
        with self.assertRaises(ValueError):
            classify_triangle(0, 2, 3)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3.0)

    def test_invalid_input2(self):
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 201)
    #ADDED
    def test_invalid_input2B(self):
        with self.assertRaises(ValueError):
            classify_triangle(201, 201, 201) 
    #ADDED
    def test_invalid_input2C(self):
        with self.assertRaises(ValueError):
            classify_triangle(201, 201, 100)

    def test_invalid_input3(self):
        with self.assertRaises(ValueError):
           classify_triangle(1, 2, -1)

    def test_invalid_input4(self):
        with self.assertRaises(ValueError):
            classify_triangle('','','')
    #ADDED
    # Test case: One side as an empty string should raise ValueError.
    def test_invalid_input4b(self):
        with self.assertRaises(ValueError):
            classify_triangle('',2,3)

    #ADDED
    def test_invalid_input4c(self):
        with self.assertRaises(ValueError):
            classify_triangle('',2,'')
        
    def test_invalid_input5(self):
        with self.assertRaises(ValueError):
            classify_triangle(None, None, None)

    def test_invalid_input6(self):
        with self.assertRaises(ValueError):
            classify_triangle(0, 0, 0)
    #ADDED

    def test_invalid_input6A(self):
        with self.assertRaises(ValueError):
            classify_triangle(0, 0, -1)

    #ADDED
    def test_invalid_input_with_side_less_than_200(self):
    # In this test case, we have a triangle with a side less than 200.
        with self.assertRaises(ValueError):
            classify_triangle(150, 220, 220)
    #ADDED but didn't help
    def test_invalid_input_with_third_side_less_than_200(self):
    # In this test case, we have a triangle with the third side less than 200.
        with self.assertRaises(ValueError):
            classify_triangle(100, 180, 230)
    #ADDED

    def test_invalid_input_with_first_side_less_than_200(self):
    # In this test case, we have a triangle with the third side less than 200.
        with self.assertRaises(ValueError):
            classify_triangle(100, 201, 230)
    #ADDED
    def test_invalid_input_with_third_side_less_than_200(self):
    # In this test case, we have a triangle with the third side less than 200.
        with self.assertRaises(ValueError):
            classify_triangle(210, 220, 100)
    #ADDED
    def test_invalid_triangle7(self):
        # Test case: Sum of any two sides less than or equal to the third side should raise ValueError.
        with self.assertRaises(ValueError):
            classify_triangle(3, 4, 7)

    def test_all_sides_greater_than_200(self):
        # Test case: All sides greater than 200 should raise ValueError.
        with self.assertRaises(ValueError):
            classify_triangle(250, 220, 300)

if __name__ == "__main__":
    my_brand(assignmentName)
    unittest.main()
    