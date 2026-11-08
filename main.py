import unittest

from mean_var_std import calculate


if __name__ == '__main__':
    print("Contoh calculate([0,1,2,3,4,5,6,7,8]):")
    for key, value in calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]).items():
        print(f"  {key}: {value}")

    print("\nMenjalankan unit test...")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_module')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
