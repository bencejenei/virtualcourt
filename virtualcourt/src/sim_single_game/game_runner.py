import virtualcourt.src.team.team_runner as team_runner
import virtualcourt.src.sim_single_game.game_helper as game_helper
from typing import Type


def main(home_team_id: str, away_team_id: str):
    home_team_card: dict = {}
    away_team_card: dict = {}
    home_team: Type[team_runner.Team] = NotImplemented
    away_team: Type[team_runner.Team] = NotImplemented

    home_team_card, away_team_card = game_helper.import_team_cards(home_team_id, away_team_id)
    home_team = game_helper.extract_team_class(home_team_card)
    away_team = game_helper.extract_team_class(away_team_card)

    home_points = int(float(game_helper.get_pts_stat(home_team)))
    away_points = int(float(game_helper.get_pts_stat(away_team)))

    game_helper.print_final_result(home_point=home_points,
                                   home_team=home_team.team_name,
                                   away_point=away_points,
                                   away_team=away_team.team_name)





if __name__ == "__main__":
    main("", "")
