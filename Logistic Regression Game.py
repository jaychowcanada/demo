# Import libraries
import random
from sklearn.linear_model import LogisticRegression

# Define the game function
def play_game():
    # Generate a random number between 0 and 9
    number = random.randint(0, 9)
    
    # Ask the user to guess the number
    guess = int(input("Guess the number between 0 and 9: "))
    
    # Train a logistic regression model on previous guesses and outcomes
    model = LogisticRegression()
    X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    y = [1 if x == number else 0 for x in X]
    model.fit(X, y)
    
    # Make a prediction using the trained model
    prediction = model.predict([[guess]])
    
    # Check if the user's guess is correct
    if prediction == 1:
        print("Congratulations, you guessed the number!")
    else:
        print(f"Sorry, the number was {number}. Better luck next time!")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")
        
# Start the game
play_game()
