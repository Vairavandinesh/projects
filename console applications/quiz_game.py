#lets create a quiz game with 4 quizzes
#the requirements
#a tuple of questions - questions are immutable thats why tuple
questions=("1. who directed GoodFellas? ",
           "2. who directed FightClub? ",
           "3. who directed The Dark Knight? ",
           "4. who directed Avatar?")
options=(("A. Martin Scorsese","B. David Fincher","C. Christopher Nolan","D. James Cameron"),
         ("A. Martin Scorsese","B. David Fincher","C. Christopher Nolan","D. James Cameron"),
         ("A. Martin Scorsese","B. David Fincher","C. Christopher Nolan","D. James Cameron"),
         ("A. Martin Scorsese","B. David Fincher","C. Christopher Nolan","D. James Cameron")
         )
#a 2 d tuple of options - each question will have 4 options and that too immutable
# a tuple of answers
answers=("A","B","C","D")
# a list of guesses by the user
guesses=[]
#a variable to store the user score
score=0
# a variable to store the current question number
question_number=0
#lets code!!!
#iterate throw the questions
for question in questions:
    print("--------------------------------------")
    print(question)
    print("--------------------------------------")
    for i in options[question_number]:
        print(i)
    guess=input("Enter your guess [A,B,C,D] : ")
    guesses.append(guess.upper())
    if guess.upper()==answers[question_number]:
        score+=1
        print("CORRECT ANSWER")
    else:
        print("WRONG ")
        print(f"{answers[question_number]} is the correct answer")
    question_number+=1
print("-----------------------------------------------")
print("--------------------RESULTS--------------------")
for i in answers:
    print(i,end=" ")
print()
for i in guesses:
    print(i,end=" ")
print()
score=(score//len(questions))*100
print(score,"%")
print("-------------------------------------------------")
print(" THANKS FOR PLAYING ")