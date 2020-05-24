
# Excel reference: https://support.office.com/en-us/article/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568

import unittest

from xlcalculator.types import XLCell
from xlcalculator import ModelCompiler
from xlcalculator import Evaluator

from . import testing

from ..xlcalculator_test import XlCalculatorTestCase


class TestPMT(XlCalculatorTestCase):

    def setUp(self):
        compiler = ModelCompiler()
        self.model = compiler.read_and_parse_archive(
            testing.get_resource("PMT.xlsx"))
        self.evaluator = Evaluator(self.model)

    def test_evaluation_A1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A1')
        value = self.evaluator.evaluate('Sheet1!A1')
        self.assertEqualTruncated( excel_value, value, 10 )

    def test_evaluation_B1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!B1')
        value = self.evaluator.evaluate('Sheet1!B1')
        self.assertEqualTruncated( excel_value, value, 10 )

    @unittest.skip("""Problem evalling: 'int' object is not callable for Sheet1!A1, PMT.pmt(Evaluator.apply("divide",eval_ref("Sheet1!A2"),12,None),eval_ref("Sheet1!A3"),eval_ref("Sheet1!A4"))""")
    def test_evaluation_C1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!C1')
        value = self.evaluator.evaluate('Sheet1!C1')
        self.assertEqual( excel_value, value )
