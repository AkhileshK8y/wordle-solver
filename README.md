# wordle-solver
Simple helper program to solve wordle puzzle.. https://www.powerlanguage.co.uk/wordle/ 

## How it works
This is a simple command line program. We have 5 letter word database in folder word_base. 

To install run..

> pip install -r requirements.txt 

Then follow the instructions of interactive CLI that starts up... 

- When you run the program i.e python main.py. 
- The program creates a file named probable_words.txt in the same folder which contains all the world in the solution space. Initial solution space is ~22000 which is all the 5 lettered english oxford dictionary words.
- Then you enter the word in wordle game and check the output. The similar word you should enter in the CLI. CLI would ask you if the world entered was correct or not. The text display would be somewhat like
> -> Is this the correct answer? If yes, then ENTER y/y else ENTER n/N...

- If the correct word is not entered then the program will ask you to enter the result you got from the wordle game. Foe each word you need to enter either 0, 1 or 2. 0 for gray, 1 for yellow and 2 for green.
- Accordingly after each turn your solution space will reduce and probable_words.txt will be updated with new set of words. Pick the next word from probable_words.txt and enter in the wordle solver.
- Repeat.
- The solution space will reduce to less than 100 after 3-4 words.


Screenshot of CLI when game is in progress show below...

![alt text](https://github.com/AkhileshK8y/wordle-solver/blob/master/game_in_progress.png)
