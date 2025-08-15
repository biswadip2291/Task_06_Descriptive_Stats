import pandas as pd

# This script is for validating the LLM's answers from Phase 1.
# It assumes the transcribed CSV files are in the project's root directory.

try:
    players_df = pd.read_csv('player_stats_2025.csv')
    games_df = pd.read_csv('game_results_2025.csv')
except FileNotFoundError:
    print("Data files not found. Please ensure they are transcribed and in the root directory.")
    exit()

print("--- Phase 1 Validation ---")

# 1. Record
total_games = len(games_df)
wins = len(games_df[games_df['Result'].str.contains('W')])
losses = total_games - wins
print(f"Record: {wins}-{losses} in {total_games} games.")

# 2. Points Leader
players_df['Pts'] = pd.to_numeric(players_df['Pts'])
points_leader = players_df.loc[players_df['Pts'].idxmax()]
print(f"Points Leader: {points_leader['Player']} with {points_leader['Pts']} points.")

# 3. CT Leader
players_df['CT'] = pd.to_numeric(players_df['CT'])
ct_leader = players_df.loc[players_df['CT'].idxmax()]
print(f"Caused Turnover Leader: {ct_leader['Player']} with {ct_leader['CT']} CT.")

print("\nValidation complete.")