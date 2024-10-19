#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests

suite = unittest.TestLoader().loadTestsFromModule(question_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

def test_get_bonus_pay_amount():
    test_cases = [
        (-1, "Invalid arguments"),   
        (200, 10),                   
        (600, 36),                   
        (1000, 70),                  
        (1500, 120),                 
        (2000, "Invalid arguments"),  
    ]

    for sales, expected in test_cases:
        result = get_bonus_pay_amount(sales)
        assert result == expected, f"For sales {sales}, expected {expected} but got {result}"

test_get_bonus_pay_amount()
print("All tests passed!")

def get_miles_per_hour():
kilometers = 32
minutes = 60
expected_result = 19.883872
result = get_miles_per_hour(kilometers, minutes)

assert abs(result - expected_result) < 1e-6, f"Expected {expected_result}, but got {result}"

print("Test passed!")
