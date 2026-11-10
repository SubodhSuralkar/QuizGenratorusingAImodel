'''
print("Welcome to the Quiz Game!")

is_user_playing = input("Do you want to play? ")

if is_user_playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
answer = input("What does ROM stands for? ").lower()

if answer == "read access memory":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
answer = input("What does HTML stands for? ").lower()

if answer == "hypertext markup language":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
answer = input("What does http stands for? ").lower()

if answer == "hypertext transfer protocol":
    print("correct answer!")
    score+=1
else:
    print("Incorrect answer!")
newscore = (score/6)  * 100
print(f"You got {score}/6 questions correct")
print(f"You have got {newscore}%.")

'''




#-----------------------------------------------------------------------------------
# this is an updated code when i realised that i should not use repeated code 
# so i used loop inside function so later 
# i can create new function with new dataset



quiz_questions = [
    {
        "question": "What does CPU stand for? ",
        "answer": "central processing unit",
    },
    {
        "question": "What does GPU stand for? ",
        "answer": "graphics processing unit",
    },
    {
        "question": "What does RAM stand for? ",
        "answer": "random access memory",
    },
    {
        "question": "What does ROM stand for? ",
        "answer": "read only memory",  # Fixed typo from original code
    },
    {
        "question": "What does HTML stand for? ",
        "answer": "hypertext markup language",
    },
    {
        "question": "What does HTTP stand for? ",
        "answer": "hypertext transfer protocol",
    },
]

def quiz(questions):
    total_questions = len(questions)
    score = 0
    for q in questions:
        user_answer = input(f"{q['question']}".lower())
        if user_answer == q["answer"]:
            print("correct answer")
            score+=1
        else:
            print("Incorrect answer")

    percentage = (score/total_questions) * 100
    print(f"{percentage} is your score! 🥹👌🙌")

user = input("Do you want to play? ").lower()
if user == "yes":
    print("Let's play 😉 \n")
    quiz(quiz_questions)
else:
    quit()