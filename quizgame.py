print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay then, let me know when you change your mind!")
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("In a website browser address bar, what does “www” stand for?  ")
if answer.lower() in ("world wide web", "worldwide web"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Originally, Amazon only sold what kind of product? ")
if answer.lower() in ("books", "book"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who painted the Mona Lisa? ")
if answer.lower() in ("leonardo da vinci", "da vinci", "leonardo davinci", "davinci"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")