# anime-quiz-project

## Purpose of project

The purpose of this project was to practice what I've learned in OOP after the 100 days course in Udemy.
The dataset I've used can be located at https://opentdb.com/api_config.php (an open-source trivia database)


## Game Description

The True/False Game is a console-based game where players are presented with a series of statements, 
and they have to determine whether each statement is true or false. The game keeps track of the player's score based on their correct and incorrect answers.

The game utilizes OOP concepts to create classes and objects for efficient code organization and functionality. The classes involved in the game include:

main: Represents the game itself and controls the flow of the game.
Question: Class function that takes in text(question) and answer
Quizbrain: This is the logic section of the game that keeps asking questions and tracks user_score 
Question_bank: The dataset that holds all the questions


The game selects questions from a predefined question bank and presents them to the player one by one. The player enters their answer, and the game evaluates it, updating the player's score accordingly. At the end of the game, the player's final score is displayed.


## Installation

To run the True/False game, follow these steps:

1. Make sure you have Python 3 installed on your system.
2. Clone or download this repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. No additional dependencies are required

## Usage
To play the True/False game, execute the following command in your terminal or command prompt from the project directory:

**python main.py**

Follow the instructions displayed on the screen. Enter "True" or "False", and press Enter to submit your answer for each question. The game will provide feedback on whether your answer is correct or incorrect. 
Once all questions are answered, the final score will be displayed.

