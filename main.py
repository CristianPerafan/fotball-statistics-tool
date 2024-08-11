from utils.season_matches import SeasonMatches
from utils.constants import COLOMBIAN_PRIMERA_A






league_name = COLOMBIAN_PRIMERA_A["league_name"]

tournament_id = COLOMBIAN_PRIMERA_A["tournament_id"]

season_id = COLOMBIAN_PRIMERA_A["season"]["2023"]

matches = SeasonMatches().get_matches_from_round_range(tournament_id, season_id, 1, 19)

matches.to_csv(f"data/{league_name}-2023_matches.csv", index=False)