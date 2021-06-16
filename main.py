import sys
import math
import itertools


class Player:
    def __init__(self, name, pocket, flank):
        self.name = name
        self._pocket = pocket
        self._flank = flank
        return

    def flank(self):
        assert self._flank >= 0
        return self._flank

    def pocket(self):
        assert self._pocket >= 0
        return self._pocket


class Team:
    def __init__(self, player_list):
        self.player_list = player_list

        if len(player_list) == 1:
            score_l = player_list[0].flank()
            score_r = player_list[0].flank()
            score_t = player_list[0].flank()
        else:
            n = math.floor(len(player_list) / 2)
            score_l = player_list[0].flank()
            for player in player_list[1:n]:
                score_l += player.pocket()
            score_r = player_list[-1].flank()
            for player in player_list[-n:-1]:
                score_r += player.pocket()
            score_t = score_l + score_r
            if len(player_list) % 2 == 1:
                score_t += player_list[n].pocket()

        self.score_l = score_l
        self.score_r = score_r
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
        l_diff = abs(team1.score_l - team2.score_l)
        r_diff = abs(team1.score_r - team2.score_r)
        t_diff = abs(team1.score_t - team2.score_t)
        if len(player_list) % 4 == 0:
            score_diff = max(l_diff, r_diff, t_diff)
        else:
            score_diff = t_diff
        if best_team_up is None or score_diff < best_team_up[2]:
            best_team_up = (team1, team2, score_diff)

    team1, team2, score_diff = best_team_up
    team1.show(prefix="team1: ")
    team2.show(prefix="team2: ")
    print(f" left wing, team1-team2={team1.score_l - team2.score_l}")
    print(f"right wing, team1-team2={team1.score_r - team2.score_r}")
    print(f"whole team, team1-team2={team1.score_t - team2.score_t}")
    team1.show(casual=True)
    team2.show(casual=True)
    return


def main():
    player_list = [
        Player("THD", 100,  90),
        Player("HBT",  -1,  80),
        Player("TTL",  80,  -1),
        Player("JCB",  -1,  60),
        Player("R04",  60,  50),
        Player("EFO",  -1,  55),
        # Player("HNH",  55,  -1),
        # Player("ZNN",  40,  40),
        # Player("SCR",  35,  -1),
        # Player("EAI",  60,  60),
    ]
    team_up(player_list)
    return


if __name__ == "__main__":
    main()
    sys.exit()
