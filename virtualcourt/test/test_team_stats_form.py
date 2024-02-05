import unittest
import virtualcourt.src.data.formatting.team_stats_form as team_stats_module
from virtualcourt.data.datafiles import team_stats_raw, team_stats_formatted


class TestBioFormatting(unittest.TestCase):
    def test_location(self):
        self.assertTrue(expr=type(team_stats_raw()) == str,
                        msg='return value of "team-stats_raw" function is not string')
        self.assertEqual(first=str(team_stats_raw())[-50:],
                         second="/virtualcourt/virtualcourt/data/raw/team_stats.csv",
                         msg="wrong path for raw file")
        self.assertTrue(expr=type(team_stats_formatted()) == str,
                        msg='return value of "team-stats_formatted" function is not string')
        self.assertEqual(first=str(team_stats_formatted())[-62:],
                         second="/virtualcourt/virtualcourt/data/formatted/team_stats_form.json",
                         msg='wrong path for formatted file')

    def test_output(self):
        self.function_output = team_stats_module.format_team_stats_file()
        self.team_id_list = list(self.function_output.keys())
        self.single_stat_items = self.function_output[self.team_id_list[0]]

        self.assertTrue(expr=type(self.function_output) == dict,
                        msg="type of return value is not dict")
        self.assertEqual(first=len(self.function_output.keys()),
                         second=30,
                         msg="Number of teams is incorrect")
        self.assertEqual(first=len(self.single_stat_items),
                         second=24,
                         msg="Number of stat items is incorrect")
        for team_id in self.team_id_list:
            self.assertEqual(first=len(self.function_output[team_id].keys()),
                             second=24,
                             msg="Some teams have incorrect amount of attributes")
            self.assertEqual(first=list(self.function_output[team_id].keys()),
                             second=['Team','G', 'MP', 'FG', 'FGA',
                                     'FG%', '3P', '3PA', '3P%', '2P',
                                     '2PA', '2P%', 'FT', 'FTA', 'FT%',
                                     'ORB', 'DRB', 'TRB', 'AST', 'STL',
                                     'BLK', 'TOV', 'PF', 'PTS'])

if __name__ == "__main__":
    unittest.main()
