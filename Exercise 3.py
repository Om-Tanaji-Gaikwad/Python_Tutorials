# Guess the number
"""
Q. Design a program to guess the number ,  Take a number n=18, set limit of guesses= 9,
  if the user guesses the number greater or smaller tell him the number is greater or smaller,
  print number of guesses ,number of guesses left , if it guesses correctly then print number
  of guesses it took to guess the number otherwise game over
"""
# Answer

n = 18
i = 1
print("Guess the number in 9 tries ")
print("Hint : The number is in between 0 to 100")
while i < 10:
    g = int(input("Your Guess : "))
    if g == n:
        print("Congratulations your guess is correct")
        print("You guessed the number in ", i, "tries")
        break
    elif g > n:
        print("Your Guess is greater than the number")
        print("Number of Guesses left : ", 9 - i)
        i = i + 1
        if i > 9:
            print("Game Over!")
    elif g < n:
        print("Your Guess is smaller than the number")
        print("Number of Guesses left : ", 9 - i)
        i = i + 1
        if i > 9:
            print("Game Over!")
    else:
        print("Invalid Input!")
