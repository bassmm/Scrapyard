scoreboard = {

}

def ReadHighScores():
    file = open("highscore.txt","r")

    file_array = file.readlines()

    for x in range(0, len(file_array), 2):
        scoreboard[file_array[x][:-1]] = int(file_array[x+1][:-1])
    file.close()


def OutputHighScores():
    for name,score in scoreboard.items():
        print(f"{name} {score}")
    

def InputNewScore():
    new_name = input("Enter Name: ")
    while len(new_name) != 3:
        new_score = (input("Please Enter a Valid 3-Digit Name: "))

    new_score = int(input("Enter Score: "))
    while new_score < 1 and new_score > 100000:
        new_score = int(input("Please Enter a Valid Score: "))                
    scoreboard[new_name] = new_score

def WritetopTen():
    new_scoreboard = dict(sorted(scoreboard.items(), key=lambda x:x[1], reverse=True))
    
    new_file = open("NewHighScore.txt","w")

    counter = 0
    for name,score in new_scoreboard.items():
        counter += 1
        if counter < 11:
            new_file.write(f"{name} {score}\n")

ReadHighScores()
OutputHighScores()
InputNewScore()
WritetopTen()