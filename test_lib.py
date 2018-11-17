import unittest
from lib import my_round


class TestLib(unittest.TestCase):
    def test_my_round_should_return_0_when_arg_is_point_5(self):
        # Given
        value_to_round = 0.5

        # When
        rounded_value = my_round(value_to_round)

        # Then
        self.assertEqual(rounded_value, 0.0)
