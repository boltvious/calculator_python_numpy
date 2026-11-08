import unittest

from mean_var_std import calculate


class MeanVarStdTestCase(unittest.TestCase):
    """Unit test mengikuti spesifikasi freeCodeCamp."""

    def test_calculate_returns_correct_statistics(self):
        actual = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [
                [6.0, 6.0, 6.0],
                [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
                6.666666666666667,
            ],
            'standard deviation': [
                [2.449489742783178, 2.449489742783178, 2.449489742783178],
                [0.816496580927726, 0.816496580927726, 0.816496580927726],
                2.581988897471611,
            ],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36],
        }
        self.assertEqual(actual, expected)

    def test_calculate_returns_lists_not_numpy_arrays(self):
        result = calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        for key, value in result.items():
            self.assertIsInstance(value, list, f"'{key}' harus berupa list")
            self.assertIsInstance(value[0], list)
            self.assertIsInstance(value[1], list)
            self.assertIsInstance(value[2], (int, float))

    def test_calculate_raises_error_for_short_list(self):
        with self.assertRaises(ValueError) as context:
            calculate([2, 6, 2, 8, 4, 0, 1, 5])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

    def test_calculate_with_negative_numbers(self):
        result = calculate([-3, -2, -1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(result['max'][2], 5)
        self.assertEqual(result['min'][2], -3)
        self.assertEqual(result['sum'][0], [0, 3, 6])


if __name__ == '__main__':
    unittest.main()
