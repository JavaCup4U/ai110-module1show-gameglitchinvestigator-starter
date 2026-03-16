# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?


- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

 - Enter key doesn’t allow me to automatically  submit a guess 
- Said to pick a number between 1 and 100 but kept telling me to go lower after 1 was entered 
- Cannot start a new game (new game button doesn’t actually start a new game ) 
- Have to reset cache in order to play a new game 
- Keeps saying to go higher and lower between two different numbers 
- Ranges for numbers aren’t paired correctly with their difficulty 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Cluade  
Claude  
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). It suggested the fix for the bug giving us the message to go lower or higher .
It suggested that the issue was that the secret number was being passed as a string instead of an integer, which caused the hints to be incorrect. I verified the result by running the tests and seeing that they all passed after implementing the suggested fix.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). I did not run into a specific misleading result or suggestion yet . 
One suggestion that ws not helpful was when I asked for help with the issue of the enter key not submitting a guess, and the AI suggested that I check for an event listener on the input field. However, this was not the issue, and I had to do further research to find the correct solution, which was to add a form around the input field and submit button. I verified this by implementing the change and testing it to see if it resolved the issue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- I decided a bug was really fixed by running the tests that I had written for that specific bug. If all the tests passed, then I was confident that the bug was fixed. Additionally, I also manually tested the game by playing it and trying to reproduce the bug to ensure that it was no longer occurring.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran was a pytest test that I wrote to check if the hints were correct after fixing the issue with the secret number being passed as a string. The test checked if the hint was "Too Low" when the guess was less than the secret number and "Too High" when the guess was greater than the secret number. After running the test, it showed me that all the assertions passed, which indicated that the hints were now correct and that the bug was fixed.
- Did AI help you design or understand any tests? How?
Yes , AI helped me design tests by suggesting specific test cases to cover different scenarios. For example, when I was testing the hints, the AI suggested that I should test for both cases where the guess is too low and too high, as well as edge cases where the guess is equal to the secret number. This helped me ensure that my tests were comprehensive and covered all possible outcomes.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because it was being generated and stored in a variable that was not persistent across Streamlit's reruns. Every time the user clicked "Submit", Streamlit would rerun the entire script, which caused the secret number to be reinitialized and thus change with each submission. This is because Streamlit does not maintain state in regular variables, and without using session state or another form of persistence, any variable will reset on each rerun.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit "reruns" refer to the fact that every time a user interacts with the app (like clicking a button or entering input), Streamlit reruns the entire script from top to bottom. This means that any variables defined in the script will be reset to their initial values unless they are stored in a special way. Session state is a feature in Streamlit that allows you to store variables that persist across these reruns. By using session state, you can keep track of information (like the secret number) even as the app reruns, which is essential for maintaining consistency in interactive applications.
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
