import virtualcourt.src.team.team_runner as team_runner
import virtualcourt.src.team.team_helper


def test():
    list_of_teams = team_runner.initial_team_class()
    team_runner.extract_data(team_id="1610612739", list_of_teams=list_of_teams)


if __name__ == "__main__":
    test()