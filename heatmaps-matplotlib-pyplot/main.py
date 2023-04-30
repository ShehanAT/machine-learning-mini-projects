import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

nhl_teams = ["Bruins", "Maple Leafs", "Lightning", "Panthers",
              "Sabres", "Senators", "Red Wings"]
nhl_team_stats = ["2022", "2021", "2020", "2019", "2018", "2017", "2016"]

nhl_games_won = np.array([[82, 63, 83, 92, 70, 45, 64],
                    [86, 48, 72, 67, 46, 42, 71],
                    [76, 89, 45, 43, 51, 38, 53],
                    [54, 56, 78, 76, 72, 80, 65],
                    [67, 49, 91, 56, 68, 40, 87],
                    [45, 70, 53, 86, 59, 63, 97],
                    [97, 67, 62, 90, 67, 78, 39]])    


fig, ax = plt.subplots()
im = ax.imshow(nhl_games_won)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(nhl_teams)), labels=nhl_teams)
ax.set_yticks(np.arange(len(nhl_team_stats)), labels=nhl_team_stats)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(nhl_teams)):
    for j in range(len(nhl_team_stats)):
        text = ax.text(j, i, nhl_games_won[i, j],
                       ha="center", va="center", color="w")

ax.set_title("NHL Games Won By Year")
fig.tight_layout(pad=0.5)
plt.show()