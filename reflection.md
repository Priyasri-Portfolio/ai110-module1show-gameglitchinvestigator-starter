# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- The first time when i played the game, few things were clearly broken. The hints were backwards. When my guess was lower than the secret number,the game incorrectly told me to "go lower", instead of "Go hihger".
- On the hard level mode the game ended before,when i still had attemps left. The secret number was keep changing every time I made a guess. It's keep changing every time. 
- I also noticed that the attempt counter starts with 1 not instead of 0.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    * I used Copilot inside VS Code as well as other resources to help me understand. AI helped me confirm the findings are actually a bug. When I played the game.I jotted down the list of bugs and then I checked with the AI's answer. One Example:One helpful suggestion was when the AI confirmed that the hints were reversed, I had already noticed this while playing the game. AI's explanation helped me verify that my observation was correct. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    * One misleading suggestion was when the AI claimed that Streamlit reruns the entire script from top to bottom on every interaction; while partially true, it didn’t fully explain why the secret number kept changing, so I had to investigate further myself.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    -I decided that the bug was fixed after i palyed the game and tested that the bug was really fixed. I see now that the hints are working correctly. After stable the steamlit, I verified that the secert number was no longer changed between guesses.  
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
    -I went over the code, and played the game. I fixed the hint bug manually. Now the hint is correctly showing for the guess > secert number ,
    as Go lower" and vice versa.  
- Did AI help you design or understand any tests? How?
      -AI help me understand parts of the code, especially around how Streamlit handles state. It pointed out that I needed to stabilize the secret number using session state, which solved one of the major issues. However, when I asked the AI to help fix the attempt counter, its suggestion actually broke the game attempts, score, and history stopped showing. So I undid that change and fixed the issue manually.
      it was making it worst, the game didn't even show the attepts,score,history. so i undid the code.




## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    -I learned that the secret number kept changing because Steamlit reruns the entire script every time
    the user interacts wit hthe app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    -Steamlit is like a automatic refresher whenever there is a change. 
- What change did you make that finally gave the game a stable secret number?
    - A stable secret number was changing that i didn't realize at first at all.
      Steamlit reran the script on every button click, which means the secret number was changing for every attempt. 
      Now the secret number dosen't change until game over.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      -One habit I want to reuse from the project is writing down the bugs with clear understanding and steps.
       to reproduce it before trying to fix anything. This was helpful for me on debugging task nad break down to AI.
       Don't want to transfer the thinking process to leave it to AI.
- What is one thing you would do differently next time you work with AI on a coding task?
  - In one or two sentences, describe how this project changed the way you think about AI generated code.
      -AI generated codes can be wrong, and make things worst. Verifying the code and understnading the AI-generated explanation
        The code verification still need human check on the code, on one of the bug fix, it removed the attemps,score,
        history and secret score. On another attempt to fix it took away the submission
