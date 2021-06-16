import sys
import math
import itertools


class Player:
    def __init__(self, name, pocket_rating, flank_rating):
        self.name = name
        self.pocket_rating = pocket_rating
        self.flank_rating = flank_rating
        return

    def pocket(self):
        assert self.pocket_rating >= 0
        return self.pocket_rating

    def flank(self):
        assert self.flank_rating >= 0
        return self.flank_rating


class Team:
    def __init__(self, player_list):
        self.player_list = player_list

        if len(player_list) == 1:
            score_w = player_list[0].flank()
            score_e = player_list[0].flank()
            score_t = player_list[0].flank()
        else:
            n = math.floor(len(player_list) / 2)
            score_w = player_list[0].flank()
            for player in player_list[1:n]:
                score_w += player.pocket()
            score_e = player_list[-1].flank()
            for player in player_list[-n:-1]:
                score_e += player.pocket()
            score_t = score_w + score_e
            if len(player_list) % 2 == 1:
                score_t += player_list[n].pocket()

        self.score_w = score_w
        self.score_e = score_e
        self.score_t = score_t
        return

    def show(self, prefix="", casual=False):
        if casual:
            log = " ".join([player.name for player in self.player_list])
        else:
            log = f"{self.player_list[0].name}({self.player_list[0].flank()}) "
            log += " ".join([f"{player.name}({player.pocket()})" for player in self.player_list[1:-1]])
            log += f" {self.player_list[-1].name}({self.player_list[-1].flank()})"
        print(f"{prefix}{log}")
        return


def team_up(player_list):
    team_size = math.ceil(len(player_list) / 2)
    best_team_up = None

    for sorted_player_list in itertools.permutations(player_list):
        try:
            team1, team2 = Team(sorted_player_list[:team_size]), Team(sorted_player_list[team_size:])
        except AssertionError:
            continue
        l_diff = abs(team1.score_w - team2.score_w)
        r_diff = abs(team1.score_e - team2.score_e)
        t_diff = abs(team1.score_t - team2.score_t)
        if len(player_list) % 4 == 0:
            score_diff = max(l_diff, r_diff, t_diff)
        else:
            score_diff = t_diff
        if best_team_up is None or score_diff < best_team_up[2]:
            best_team_up = (team1, team2, score_diff)

    team1, team2, score_diff = best_team_up
    print("[Details]")
    team1.show(prefix="team1: ")
    team2.show(prefix="team2: ")
    print(f" west wing: team1-team2={team1.score_w - team2.score_w}")
    print(f" east wing: team1-team2={team1.score_e - team2.score_e}")
    print(f"whole team: team1-team2={team1.score_t - team2.score_t}")
    print("\n[Result]")
    team1.show(casual=True)
    team2.show(casual=True)
    return


def main():
    player_list = [
        Player("THD", pocket_rating=100, flank_rating= 90),
        Player("HBT", pocket_rating= -1, flank_rating= 80),
        Player("TTL", pocket_rating= 80, flank_rating= -1),
        Player("JCB", pocket_rating= -1, flank_rating= 60),
        Player("R04", pocket_rating= 60, flank_rating= 50),
        Player("EFO", pocket_rating= -1, flank_rating= 55),
        Player("HNH", pocket_rating= 55, flank_rating= -1),
        Player("ZNN", pocket_rating= 40, flank_rating= 40),
        # Player("SCR", pocket_rating= 35, flank_rating= -1),
        # Player("EAI", pocket_rating= 60, flank_rating= 60),
    ]
    team_up(player_list)
    return


if __name__ == "__main__":
    main()
    sys.exit()
