import unittest
import virtualcourt.src.data.formatting.team_bio_form as bio_module
from virtualcourt.data.datafiles import team_bio_raw, team_bio_formatted


class TestBioFormatting(unittest.TestCase):
    def test_location(self):
        self.assertTrue(type(team_bio_raw()) == str, 'return value of "team-bio_raw" function is not string')
        self.assertEqual(first=team_bio_raw(),
                         second="/Users/jeneibence/Desktop/BENCE/RABBITHOLES/virtualcourt/virtualcourt/data/raw/team_bio.json",
                         msg="wrong path")
        self.assertTrue(type(team_bio_formatted()) == str,
                        'return value of "team-bio_formatted" function is not string')
        self.assertEqual(first=team_bio_raw(),
                         second="/Users/jeneibence/Desktop/BENCE/RABBITHOLES/virtualcourt/virtualcourt/data/raw/team_bio.json",
                         msg='wrong path')

    def test_output(self):
        self.function_output = bio_module.format_team_bio_file()
        self.team_id_list = list(self.function_output.keys())
        self.single_bio_items = self.function_output[self.team_id_list[0]]

        self.assertTrue(type(self.function_output) == dict,
                        "type of return value is not dict")
        self.assertEqual(first=len(self.function_output.keys()),
                         second=30,
                         msg="Number of teams is incorrect")
        self.assertEqual(first=len(self.single_bio_items),
                         second=8)
        for team_id in self.team_id_list:
            self.assertEqual(first=len(self.function_output[team_id].keys()),
                             second=8,
                             msg="Some teams have incorrect amount of attributes")
            self.assertEqual(first=list(self.function_output[team_id].keys()),
                             second=['team_id', 'team_tag', 'team_nickname', 'team_establishment', 'team_city', 'team_name', 'team_state', 'team_championship_years'])


if __name__ == "__main__":
    unittest.main()
