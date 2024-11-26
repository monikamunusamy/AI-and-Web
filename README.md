# Fruit Detective: Crack the Code

Welcome to **Fruit Detective**! An interactive guessing game where players try to guess the name of a fruit based on hints provided by an AI assistant. You can enjoy the game and sharpen your fruit knowledge while having fun!

![Webpage Screenshot](https://github.com/monikamunusamy/AI-and-Web/blob/main/images/Homepage.jpg)

## Key Features

- **Interactive Gameplay**: Enjoy an engaging guessing game ideal for all ages.
- **Hints Provided**: Stuck on a guess? Type 'hint' to get a clue!
- **User-Friendly Interface**: Smooth navigation ensures a delightful user experience.
- **Powered by AI**: Utilize OpenAI's capabilities to enhance your gameplay.

## Getting Started

Follow these steps to get your **Fruit Detective** game up and running.

### 1. Clone the Repository

You can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/monikamunusamy/AI-and-Web.git
cd AI-and-Web
```

### 2. Install the Dependencies

Ensure you have Python 3.10+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

To start playing the game, run the following command:

```bash
streamlit run app.py
```

### Project Structure

```
monikamunusamy/
├── pages/                      # Contains different game pages
│   ├── Play.py                 # Chat interface and game logic
│   ├── Stats.py                # Statistics dashboard
├── data/                       # Contains datasets and JSON files
│   ├── session_state.json      # JSON file for saving session state
│   └── play_screenshot.png     # Screenshot for README
├── images/                     # Directory for images
│   ├── Background.jpg          # Application Background
│   ├── homepage.jpg             # Screenshot of application homepage
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
```

### Acknowledgment

- [Streamlit](https://streamlit.io/) for the interactive web app framework.
- [OpenAI](https://openai.com/) for the GPT-4o-mini language model.


