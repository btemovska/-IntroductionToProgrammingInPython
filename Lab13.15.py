class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return team_wins / (team_wins + team_losses)


if __name__ == "__main__":

    team = Team()

    team_name = 'Angels'
    team_wins = 80
    team_losses = 82

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')



