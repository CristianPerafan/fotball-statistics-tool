from utils.constants import SOFA_SCORE_API_BASE_URL
import requests
import pandas as pd



class SeasonMatches:
    def __init__(self, ):
        self.url = SOFA_SCORE_API_BASE_URL

    def get_matches_by_round(self, tournament_id, season_id, round_id):
        response = requests.get(f"{self.url}unique-tournament/{tournament_id}/season/{season_id}/events/round/{round_id}")
        events = response.json().get("events")
        matches = []
        for event in events:

            finished = event.get("status").get("type") == "finished"
    
            if finished:
                
                match = {
                    "Home Team": event.get("homeTeam").get("name"),
                    "Home Team Slug": event.get("homeTeam").get("slug"),
                    "Away Team": event.get("awayTeam").get("name"),
                    "Away Team Slug": event.get("awayTeam").get("slug"),
                    "Home Score": event.get("homeScore").get("current"),
                    "Away Score": event.get("awayScore").get("current"),
                    "Total Goals": event.get("homeScore").get("current") + event.get("awayScore").get("current"),
                    "Match ID": event.get("id"),
                    "Round": round_id
                }
                matches.append(match)
                
        df = pd.DataFrame(matches, 
                          columns=["Home Team", "Home Team Slug", "Away Team", 
                                   "Away Team Slug", "Home Score", "Away Score", "Total Goals", "Round",
                                   "Match ID"]
                        )
        return df
        
    def get_matches_from_round_range(self, tournament_id, season_id, start_round, end_round):
        matches = []
        for round_id in range(start_round, end_round+1):
            matches.append(self.get_matches_by_round(tournament_id, season_id, round_id))
        


        range_matches = pd.concat(matches)
        return range_matches
        

