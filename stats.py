import streamlit as st
import os
import json
from collections import defaultdict

# File path for saving statistics
SAVE_FILE_PATH = "data/session_stats.json"

# Initialize session state and statistics
if "initialized" not in st.session_state:
    st.session_state["guesses"] = defaultdict(list)
    st.session_state["game_count"] = 0
    st.session_state["current_game_guesses"] = 0
    st.session_state["games_won"] = 0
    st.session_state["games_played"] = 0
    st.session_state["initialized"] = True

# Function to load statistics from file
def load_stats():
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "r") as file:
            return json.load(file)
    return {"games_played": 0, "games_won": 0, "guesses": []}

# Function to save statistics to file
def save_stats(stats):
    os.makedirs(os.path.dirname(SAVE_FILE_PATH), exist_ok=True)
    with open(SAVE_FILE_PATH, "w") as file:
        json.dump(stats, file)

# Load stats on app start
stats = load_stats()

# Save current game data (simulate game logic)
if "current_game_guesses" in st.session_state and st.session_state["current_game_guesses"] > 0:
    stats["games_played"] += 1
    stats["guesses"].append(st.session_state["current_game_guesses"])
    if st.session_state.get("game_won", False):
        stats["games_won"] += 1
    save_stats(stats)
    st.session_state["current_game_guesses"] = 0  # Reset after saving

# Display the Statistics Page
st.title("Game Statistics")

# Display total games played and won
st.metric("Games Played", stats["games_played"])
st.metric("Games Won", stats["games_won"])

# Display average guesses per game
if stats["games_played"] > 0:
    avg_guesses = sum(stats["guesses"]) / stats["games_played"]
    st.metric("Average Guesses per Game", f"{avg_guesses:.2f}")
    st.write("Game-by-Game Details:")
    for i, guesses in enumerate(stats["guesses"], start=1):
        st.write(f"Game {i}: {guesses} guesses")
else:
    st.write("No games played yet.")