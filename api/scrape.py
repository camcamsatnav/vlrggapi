from api.scrapers import (
    check_health,
    vlr_live_score,
    vlr_match_results,
    vlr_news,
    vlr_rankings,
    vlr_stats,
    vlr_upcoming_matches,
)


class Vlr:
    @staticmethod
    def vlr_news():
        return vlr_news()

    @staticmethod
    def vlr_rankings(region):
        return vlr_rankings(region)

    @staticmethod
    def vlr_stats(region: str, timespan: str, min_rounds: str, min_rating: str, event_id: str):
        return vlr_stats(region, timespan, min_rounds, min_rating, event_id)

    @staticmethod
    def vlr_upcoming_matches():
        return vlr_upcoming_matches()

    @staticmethod
    def vlr_live_score():
        return vlr_live_score()

    @staticmethod
    def vlr_match_results():
        return vlr_match_results()

    @staticmethod
    def check_health():
        return check_health()


if __name__ == "__main__":
    print(Vlr.vlr_live_score())
