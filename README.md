# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose. 
The purpose of the game is to guess a secret number between 1 and 100. The player inputs their guess, and the game provides hints whether the guess is too high, too low, or correct. The player wins by guessing the correct number.
- [ ] Detail which bugs you found.
The issues: 
 Enter key doesn’t allow me to automatically  submit a guess 
- Said to pick a number between 1 and 100 but kept telling me to go lower after 1 was entered 
- Cannot start a new game (new game button doesn’t actually start a new game ) 
- Have to reset cache in order to play a new game 
- Keeps saying to go higher and lower between two different numbers 
- Ranges for numbers aren’t paired correctly with their difficulty 
- [ ] Explain what fixes you applied.
The fixes I applied include:
Fixed and refactored the check_guess function and moved it to logic_utils.py. 
-Fixed the lexographic comparison issue by ensuring that the secret number is stored and compared as an integer rather than a string.


## 📸 Demo

- [ ] ![Pytest Results](images/Screenshot%202026-03-14%20at%207.09.54 PM.png)  


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
