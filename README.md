# Team Utilities

Create two ordered teams for a list of players according to their skill levels.

For example, 8 players can setup the following battle:

- team1: west-flank, west-pocket, east-pocket, east-flank
- team2: west-flank, west-pocket, east-pocket, east-flank

## Balance Considerations

- The mean (positional) skill ratings of the teams are balanced.
- (A Player's pocket and flank ratings can be different.)
- The mean skill ratings of each wing are also balanced when there are no central players.
- (Central players do not belong to any wing and render wing balance less important.)

## Running the Tool

In main():
```python
player_list = [
    Player("THD", pocket_rating=100, flank_rating= 90),
    Player("HBT", pocket_rating= -1, flank_rating= 80),
    Player("TTL", pocket_rating= 80, flank_rating= -1),
    Player("JCB", pocket_rating= -1, flank_rating= 60),
    Player("R04", pocket_rating= 60, flank_rating= 50),
    Player("EFO", pocket_rating= -1, flank_rating= 55),
    Player("HNH", pocket_rating= 55, flank_rating= -1),
    Player("ZNN", pocket_rating= 40, flank_rating= 40),
]
team_up(player_list)
```

Output:
```
[Details]
team1: THD(90) HNH(55) R04(60) EFO(55)
team2: JCB(60) TTL(80) ZNN(40) HBT(80)
 west wing: team1-team2=5
 east wing: team1-team2=-5
whole team: team1-team2=0

[Result]
THD HNH R04 EFO
JCB TTL ZNN HBT
```
