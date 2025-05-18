import unittest
import importlib
import sqlite3
import pandas as pd

class TestAssignment(unittest.TestCase):
    def test_01(self):
        presidents_taipei_xlsx = asgmt.import_presidents_taipei_xlsx()
        self.assertEqual(len(presidents_taipei_xlsx.shape), 2)
    def test_02(self):
        candidates = asgmt.retrieve_candidates_from_presidents_taipei_xlsx()
        self.assertEqual(candidates.shape, (3, 3))
        presidents = candidates.iloc[:, 1].values
        vice_presidents = candidates.iloc[:, 2].values
        for p in ["柯文哲", "賴清德", "侯友宜"]:
            self.assertIn(p, presidents)
        for vp in ["吳欣盈", "蕭美琴", "趙少康"]:
            self.assertIn(vp, vice_presidents)
    def test_03(self):
        towns = asgmt.retrieve_towns_from_presidents_taipei_xlsx()
        self.assertEqual(towns.shape, (12,))
        for d in ["中正區", "中山區", "大同區", "大安區", "萬華區", "士林區"]:
            self.assertIn(d, towns.values.tolist())
    def test_04(self):
        votes_by_candidates = asgmt.summarize_votes_by_candidates_from_presidents_taipei_xlsx()
        self.assertEqual(votes_by_candidates.shape, (3, 4))
        presidents = votes_by_candidates.iloc[:, 1].values
        vice_presidents = votes_by_candidates.iloc[:, 2].values
        votes = votes_by_candidates.iloc[:, 3].values
        for p in ["柯文哲", "賴清德", "侯友宜"]:
            self.assertIn(p, presidents)
        for vp in ["吳欣盈", "蕭美琴", "趙少康"]:
            self.assertIn(vp, vice_presidents)
        for v in [366854, 587899, 587258]:
            self.assertIn(v, votes)
    def test_05(self):
        votes_by_towns = asgmt.summarize_votes_by_towns_from_presidents_taipei_xlsx(1)
        self.assertEqual(votes_by_towns.shape, (12, 5))
        votes_by_towns = asgmt.summarize_votes_by_towns_from_presidents_taipei_xlsx(2)
        self.assertEqual(votes_by_towns.shape, (12, 5))
        votes_by_towns = asgmt.summarize_votes_by_towns_from_presidents_taipei_xlsx(3)
        self.assertEqual(votes_by_towns.shape, (12, 5))
    def test_06(self):
        electoral_districts = asgmt.retrieve_electoral_districts_from_regional_legislators_taipei_xlsx()
        self.assertIsInstance(electoral_districts, list)
        self.assertEqual(len(electoral_districts), 8)
        for i in range(1, 9):
            self.assertIn(f"臺北市第{i}選舉區", electoral_districts)
    def test_07(self):
        candidates = asgmt.retrieve_candidates_from_regional_legislators_taipei_xlsx()
        self.assertIsInstance(candidates, list)
        self.assertEqual(len(candidates), 53)
        for cand in ["吳思瑤", "王世堅", "王鴻薇", "李彥秀", "吳沛憶", "羅智強", "徐巧芯", "賴士葆"]:
            self.assertIn(cand, candidates)
    def test_08(self):
        candidates_and_parties = asgmt.retrieve_candidates_and_parties_from_regional_legislators_taipei_xlsx()
        self.assertEqual(candidates_and_parties.shape, (53, 3))
        for i in range(1, 9):
            self.assertIn(f"臺北市第{i}選舉區", candidates_and_parties.iloc[:, 0].values.tolist())
        for p in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟"]:
            self.assertIn(p, candidates_and_parties.iloc[:, 1].values.tolist())
        for cand in ["吳思瑤", "王世堅", "王鴻薇", "李彥秀", "吳沛憶", "羅智強", "徐巧芯", "賴士葆"]:
            self.assertIn(cand, candidates_and_parties.iloc[:, 2].values.tolist())
    def test_09(self):
        votes_received = asgmt.retrieve_votes_received_from_regional_legislators_taipei_xlsx()
        self.assertEqual(votes_received.shape, (53, 4))
        for i in range(1, 9):
            self.assertIn(f"臺北市第{i}選舉區", votes_received.iloc[:, 0].values.tolist())
        for p in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟"]:
            self.assertIn(p, votes_received.iloc[:, 1].values.tolist())
        for cand in ["吳思瑤", "王世堅", "王鴻薇", "李彥秀", "吳沛憶", "羅智強", "徐巧芯", "賴士葆"]:
            self.assertIn(cand, votes_received.iloc[:, 2].values.tolist())
        for v in [91958, 111605, 105050, 112743, 66932, 87973, 89727, 87099]:
            self.assertIn(v, votes_received.iloc[:, 3].values.tolist())
    def test_10(self):
        elected = asgmt.retrieve_elected_from_regional_legislators_taipei_xlsx()
        self.assertEqual(elected.shape, (8, 4))
        for i in range(1, 9):
            self.assertIn(f"臺北市第{i}選舉區", elected.iloc[:, 0].values.tolist())
        for p in ["民主進步黨", "中國國民黨"]:
            self.assertIn(p, elected.iloc[:, 1].values.tolist())
        for cand in ["吳思瑤", "王世堅", "王鴻薇", "李彥秀", "吳沛憶", "羅智強", "徐巧芯", "賴士葆"]:
            self.assertIn(cand, elected.iloc[:, 2].values.tolist())
        for v in [91958, 111605, 105050, 112743, 66932, 87973, 89727, 87099]:
            self.assertIn(v, elected.iloc[:, 3].values.tolist())
        
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignment)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")