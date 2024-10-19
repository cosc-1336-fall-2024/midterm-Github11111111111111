#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests

suite = unittest.TestLoader().loadTestsFromModule(question_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

def test_get_bonus_pay_amount():
    test_cases = [
        (-1, "Invalid arguments"),   # Test case for sales less than 0
        (200, 10),                   # 200 should return bonus of 10
        (600, 36),                   # 600 should return bonus of 36
        (1000, 70),                  # 1000 should return bonus of 70
        (1500, 120),                 # 1500 should return bonus of 120
        (2000, "Invalid arguments"),  # Test case for sales greater than 1999
    ]

    for sales, expected in test_cases:
        result = get_bonus_pay_amount(sales)
        assert result == expected, f"For sales {sales}, expected {expected} but got {result}"

# Run the tests
test_get_bonus_pay_amount()
print("All tests passed!")
