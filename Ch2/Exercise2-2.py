# display a title
print("The Test Scores Program")
print()
print("Enter 3 test scores")
print("=====================")

# get scores from the user and accumulate the total

score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
totalScore = score1 + score2 + score3

# Calulate average score
averageScore = round(totalScore / 3)

# Format and display the result
print("=====================")
print("Your Scores: ", score1, score2, score3)
print("Total Score:   ", totalScore,
      "\nAverage Score:  ", averageScore)
print()
print("Bye")