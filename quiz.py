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


"""

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

"""
#-----------------------------------------------------------------------------=======================================================
#ahumm ahumm so i wanted to do something special so i added ai modeelllll to genrate questions instead of predefined dataset so it can genrate quiz on any topic
# hehe this is so much better feelin like got a upgrade from square to round tires 

import json

from google import genai

client = genai.Client(api_key="Paste you API key here")

def get_ai_question(topic):
    prompt=f"""  Create 10 Quiz Question about {topic} 
                return only a raw json array of objects like this:
                [
                {{"question": "What does CPU stand for? ", "answer": "central processing unit"}}
                ]
                Keep answers direct, short, and lowercase.
"""
    response = client.models.generate_content(
        model="gemini-3.6-flash",contents=prompt
    )
    raw_text = response.text.strip().strip('`').replace("json","").strip()
    return json.loads(raw_text)

def quiz(question):

    total_questions = len(question)
    score = 0 
    for q in question:
        user_answer = input(f"{q['question']}" .lower())
        if user_answer == q['answer']:
            print('Correct Answer')
            score += 1
        else:
            print("Incorrect Answer")

    percent = (score/total_questions) *100
    print(f"You got {percent}%. 🥹👌🙌")

user_input = input("Do you wanna play? ").lower().strip()
if user_input == 'yes':
    topic =input("What do you want the quiz to be about? \n Enter the topic--> ")
    print("Processing-------%----")
    try:
        ai_questions = get_ai_question(topic)
        quiz(ai_questions)
    except Exception as e:
        print(f"Error generating AI questions: {e}")
        print("Falling back to default questions...\n")
else:
    print("Let's play Next time")
    quit()

#first tine ritinfwriting the code ALL BY MY OWN HANDS FOR 3 HOURS CONSISTENTLY FINDING AND SOLVING BUGS