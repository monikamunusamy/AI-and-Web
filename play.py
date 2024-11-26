import streamlit as st
import pandas as pd
import json
import os
from collections import defaultdict

# File to save statistics
SAVE_FILE_PATH = "data/session_stats.json"

# Load or initialize statistics
def load_stats():
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "r") as file:
            return json.load(file)
    return {"games_played": 0, "games_won": 0, "guesses": [], "hints": []}

def save_stats(stats):
    os.makedirs(os.path.dirname(SAVE_FILE_PATH), exist_ok=True)
    with open(SAVE_FILE_PATH, "w") as file:
        json.dump(stats, file)

# Load game stats
stats = load_stats()

# Sidebar for API Key
st.sidebar.title("🔑 API Key")
st.session_state["openai_api_key"] = st.sidebar.text_input(
    "Enter OpenAI API Key", 
    type="password", 
    value=st.session_state.get("openai_api_key", "")
)
if not st.session_state["openai_api_key"]:
    st.sidebar.warning("⚠ Please enter your OpenAI API Key to proceed.")
# Add Fruits Background with Adjustable Transparency and Font Style
def add_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                rgba(225, 225, 225, 0.8), 
                rgba(255, 255, 255, 0.8)
            ), 
            url("https://img.freepik.com/free-psd/3d-illustration-with-berries-still-life_23-2151385119.jpg");
            background-size: cover;
            background-attachment: fixed;
        }
        h1 {
            font-family: 'Arial', sans-serif;
            color: #FF6347; /* Brighter color */
            text-align: center;
            font-size: 3em;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Nice shadow */
        }
        h2 {
            font-family: 'Arial', sans-serif;
            color: #FF4500; /* Dark orange */
            font-size: 2.5em; 
            text-align: center;
            margin-bottom: 15px;
        }
        h3 {
            font-family: 'Arial', sans-serif;
            color: #4682B4; /* Steel Blue */
            font-size: 2em; 
            text-align: left; 
        }
        .sidebar-content {
            background-color: rgba(255, 255, 255, 0.9); /* Sidebar with a light tint */
            color: #000000; /* Text color in the sidebar */
        }
        .stButton {
            background-color: #1E90FF; /* Button background color */
            color: white; /* Button text color */
            border-radius: 5px; /* Round edges of buttons */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
add_background_image()
# Fruits Dataset
@st.cache_data
def load_fruit_data():
    # Sample dataset of fruits
    data = [
    {"name": "Apple", "color": "Red or Green", "taste": "Sweet or Tart", "type": "Pome", "origin": "Central Asia"},
    {"name": "Banana", "color": "Yellow", "taste": "Sweet", "type": "Berry", "origin": "Southeast Asia"},
    {"name": "Cherry", "color": "Red", "taste": "Sweet or Tart", "type": "Drupe", "origin": "Europe/Asia"},
    {"name": "Orange", "color": "Orange", "taste": "Citrusy", "type": "Citrus", "origin": "China"},
    {"name": "Pineapple", "color": "Yellow with Green Leaves", "taste": "Sweet and Tart", "type": "Multiple Fruit", "origin": "South America"},
    {"name": "Mango", "color": "Yellow, Green, or Red", "taste": "Sweet", "type": "Drupe", "origin": "South Asia"},
    {"name": "Fig", "color": "Purple or Green", "taste": "Sweet", "type": "Multiple Fruit", "origin": "Western Asia"},
    {"name": "Kiwi", "color": "Brown (with Green Flesh)", "taste": "Sweet and Tart", "type": "Berry", "origin": "China/New Zealand"},
    {"name": "Guava", "color": "Green or Yellow", "taste": "Sweet", "type": "Berry", "origin": "Central America"},
    {"name": "Papaya", "color": "Orange or Yellow", "taste": "Sweet", "type": "Berry", "origin": "Central America"},
    {"name": "Peach", "color": "Pink or Yellow", "taste": "Sweet", "type": "Drupe", "origin": "China"},
    {"name": "Grapes", "color": "Green, Red, or Black", "taste": "Sweet or Tart", "type": "Berry", "origin": "Near East"}
]
    return pd.DataFrame(data)

fruit_data = load_fruit_data()

# Fix: Select a truly random fruit
def pick_random_fruit():
    """Selects a truly random fruit from the dataset."""
    return fruit_data.sample(1).iloc[0]

# Reset session state for a new game
def reset_session_state():
    st.session_state["messages"] = [{"role": "assistant", "content": "🍇 Hello there! Let’s play a guessing game! Ask insightful questions to help figure out the fruit!."}]
    st.session_state["selected_fruit"] = pick_random_fruit()
    st.session_state["game_over"] = False
    st.session_state["current_game_guesses"] = 0
    st.session_state["current_game_hints"] = 0

# Handle correct guesses
def correct_guess():
    st.session_state["game_over"] = True
    stats["games_played"] += 1
    stats["games_won"] += 1
    stats["guesses"].append(st.session_state["current_game_guesses"])
    stats["hints"].append(st.session_state["current_game_hints"])
    save_stats(stats)

# Handle incorrect guesses
def incorrect_guess():
    st.session_state["current_game_guesses"] += 1

# Provide a hint
def give_hint():
    fruit = st.session_state["selected_fruit"]

    hints = [
        f"🔍 Hint: The fruit's color is {fruit['color']}.",
        f"🔍 Hint: The fruit's taste is {fruit['taste']}.",
        f"🔍 Hint: The fruit belongs to the {fruit['type']} type.",
        f"🔍 Hint: The fruit originates from {fruit['origin']}."

    ]

    hint_index = st.session_state["current_game_hints"]
    if hint_index < len(hints):
        st.session_state["current_game_hints"] += 1
        return hints[hint_index]
    
    return "🔍 No more hints available!"

# Initialize session state
if "messages" not in st.session_state:
    reset_session_state()

# Page Layout
if st.session_state["openai_api_key"]:
    page = st.sidebar.radio("📋 Navigate", ["🎮 Play Game", "📊 Statistics"])

    if page == "🎮 Play Game":
        st.title("🍇 Fruit Detective: Crack the Code!?")
        st.write("💡 Guess the fruit based on hints. Type 'hint' to get a clue!")

        # Display chat messages
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        # Handle game logic
        if not st.session_state["game_over"]:
            user_input = st.chat_input("Your guess or type 'hint' for a clue:")
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.chat_message("user").write(user_input)

                fruit = st.session_state["selected_fruit"]
                if user_input.lower() == fruit["name"].lower():
                    msg = f"🎉 Correct! It's {fruit['name']}!"
                    correct_guess()
                elif user_input.lower() == "hint":
                    msg = give_hint()
                else:
                    msg = "❌ Incorrect! Try again or ask for a hint."
                    incorrect_guess()

                st.session_state.messages.append({"role": "assistant", "content": msg})
                st.chat_message("assistant").write(msg)

        if st.session_state["game_over"]:
            st.button("🔄 Play Again", on_click=reset_session_state)

    elif page == "📊 Statistics":
        st.title("📊 Game Statistics")
        st.metric("🎮 Games Played", stats["games_played"])
        st.metric("🏆 Games Won", stats["games_won"])

        if stats["games_played"] > 0:
            avg_guesses = sum(stats["guesses"]) / stats["games_played"]
            avg_hints = sum(stats["hints"]) / stats["games_played"]
            st.metric("🔢 Average Guesses per Game", f"{avg_guesses:.2f}")
            st.metric("💡 Average Hints per Game", f"{avg_hints:.2f}")

            st.write("📜 *Game-by-Game Details:*")
            for i, (guesses, hints) in enumerate(zip(stats["guesses"], stats["hints"]), start=1):
                st.write(f"🎮 *Game {i}:* {guesses} guesses, {hints} hints")
        else:
            st.write("No games played yet. Start playing to track your progress!")
else:
    st.title("🔑 API Key Required")
    st.write("Please enter your OpenAI API Key in the sidebar to start playing.")
    st.warning("⚠ API Key is required to proceed!")