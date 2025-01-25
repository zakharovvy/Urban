import unittest
import tests_12_2

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(tests_12_2)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
