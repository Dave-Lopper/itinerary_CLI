import unittest


class TestManager():
    def test(self):
        tests = unittest \
            .TestLoader() \
            .discover('src/tests/', pattern='*test.py')

        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            return 0
        return 1
