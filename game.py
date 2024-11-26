import streamlit as st
import random

# Ask for the username (only once when the app is first run)
if "username" not in st.session_state:
    st.session_state.username = st.text_input("Enter your name:", "")
    if st.session_state.username:
        st.session_state.game_started = True
    else:
        st.session_state.game_started = False

# If game is not started yet, ask the user to enter their name
if not st.session_state.game_started:
    st.write("Please enter your name to start playing.")
else:
    # Initialize the game state (if not already initialized)
    if "selected_fruit" not in st.session_state:
        st.session_state.selected_fruit = random.choice(["Apple", "Banana", "Cherry", "Mango", "Pineapple"])
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.session_state.messages = [{"role": "assistant", "content": f"Welcome to the Guess the Fruit game, {st.session_state.username}! Type your guess below."}]
    
    # Function to check the guess
    def check_guess(user_guess):
        if user_guess.strip().lower() == st.session_state.selected_fruit.lower():
            st.session_state.game_over = True
            return f"Correct, {st.session_state.username}! It's a {st.session_state.selected_fruit}!"
        else:
            return "Incorrect guess. Try again!"

    # Reset game state when "Play Again" is clicked
    def reset_game():
        st.session_state.selected_fruit = random.choice(["Apple", "Banana", "Cherry", "Mango", "Pineapple"])
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.session_state.messages = [{"role": "assistant", "content": f"Welcome back, {st.session_state.username}! Type your guess below."}]

    # Display game title and score
    st.title("🍎 Guess the Fruit!")
    st.write(f"Your Guesses: {st.session_state.guesses}")

    # Display chat history (messages exchanged so far)
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # If game is over, show the "Play Again" button
    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game()

    # Accept user guess input as a chat message
    user_guess = st.chat_input("Your guess (type the fruit name):")
    if user_guess:
        st.session_state.guesses += 1
        feedback = check_guess(user_guess)
        
        # Append user input and feedback to chat history
        st.session_state.messages.append({"role": "user", "content": user_guess})
        st.session_state.messages.append({"role": "assistant", "content": feedback})

        # Show feedback in the chat
        st.chat_message("assistant").write(feedback)
