import unittest

import HtmlTestRunner

from unit_tests.test_correct_url_navigation import CorrectUrlNavigation
from unit_tests.test_sort_menu import SortFunctionality


class TestSuite(unittest.TestCase):

    # cream metoda de executie
    def test_suite(self):

        # instantiem obiect din suita
        teste_de_rulat = unittest.TestSuite()

        # adaugam clasele de teste care vrem sa fie executate
        teste_de_rulat.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(SortFunctionality),
                unittest.defaultTestLoader.loadTestsFromTestCase(CorrectUrlNavigation),
            ]
        )

        # teste_de_rulat.addTest(
        #     unittest.defaultTestLoader.loadTestsFromTestCase(SortFunctionality)
        # )

        # cream raportul de executie
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Emag Functionality Tests",
            report_name="Regression",
        )

        # rularea raportului de executie
        runner.run(teste_de_rulat)
