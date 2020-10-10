#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    score_list = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  score_list
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                score_list.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(score_list):
    score_total = 0
    count = len(score_list)

    for score in score_list:
        score_total += score

    # calculate average score
    average = score_total / count

    # get min/max
    low_score = min(score_list)
    high_score = max(score_list)

    # get median
    median_index = len(score_list) // 2
    if len(score_list) % 2 == 1:  # odd
        median_score = score_list[median_index]
    else:                     # even
        middle1 = score_list[median_index]
        middle2 = score_list[median_index-1]
        median_score = (middle1 + middle2)/2

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median_score)

def main():
    display_welcome()
    score_list = get_scores()
    process_scores(score_list)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


