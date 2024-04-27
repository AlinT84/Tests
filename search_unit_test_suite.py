import unittest

import HtmlTestRunner

from unit_tests.test_sort_menu import SearchFunctionality


class TestSuite(unittest.TestCase):

    # cream metoda de executie
    def test_suite(self):

        # instantiem obiect din suita
        teste_de_rulat = unittest.TestSuite()

        # adaugam clasele de teste care vrem sa fie executate
        # teste_de_rulat.addTests(
        #     [
        #         unittest.defaultTestLoader.loadTestsFromTestCase(Test_Alerts),
        #         unittest.defaultTestLoader.loadTestsFromTestCase(Test_Keys),
        #         unittest.defaultTestLoader.loadTestsFromTestCase(Login_functionality),
        #     ]
        # )

        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(SearchFunctionality))
        # teste_de_rulat.addTest(
        #     unittest.defaultTestLoader.loadTestsFromTestCase(Test_Alerts)
        # )

        # cream raportul de executie
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Search Functionality Tests",
            report_name="Regression",
        )

        # rularea raportului de executie
        runner.run(teste_de_rulat)
