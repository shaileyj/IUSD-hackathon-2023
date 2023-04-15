import hmm
# I changed things! MWAHAHAHAHAHA
subject = input("What subject do you want multiple choice questions on?\n")
json_data = hmm.get_questions(subject)

for question in json_data["questions"]:
    print()
    print(question["question"])
    for option in question["options"]:
        print(option)
    guess = input()
    if guess.upper() == question["answer"].upper():
        print("correct!", question["explanation"])
    else:
        print("incorrect. The correct answer was", question["answer"], question["explanation"])

