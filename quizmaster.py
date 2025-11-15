import pgzrun

WIDTH = 1000
HEIGHT = 600

gameover = False
questions=[]
score=0
timer=10
questionfile = "Lesson 9-QuizMaster\questions.txt"
marqueebox = Rect(0,0,1000,90)
behindbox = Rect(0,0,1000,90)
questionbox = Rect(10,100,610,100)
answerbox1 = Rect(10,210,300,150)
answerbox2 = Rect(10,370,300,150)
answerbox3 = Rect(320,210,300,150)
answerbox4 = Rect(320,370,300,150)
scorebox = Rect(700,100,250,100)
skipbox = Rect(700,400,250,100)
timerbox = Rect(700,250,250,100)
answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]

def draw():
    screen.fill("red")
    screen.draw.filled_rect(behindbox,"pink")
    screen.draw.filled_rect(marqueebox,"pink")
    screen.draw.textbox("Welcome to the QuizMaster",marqueebox,color="blue")
    screen.draw.filled_rect(questionbox,"light blue")
    screen.draw.textbox(question[0].strip(),questionbox,color="purple")
    index=1
    for i in answerboxes:
        screen.draw.filled_rect(i,"green")
        screen.draw.textbox(question[index].strip(),i,color="blue")
        index+=1
    screen.draw.filled_rect(timerbox,"yellow")
    screen.draw.textbox(str(timer),timerbox,color="red")
    screen.draw.filled_rect(scorebox,"yellow")
    screen.draw.textbox("score:"+str(score),scorebox,color="black")
    screen.draw.filled_rect(skipbox,"orange")
    screen.draw.textbox("skip",skipbox,color="pink")
    if gameover:
        screen.fill("pink")
        screen.draw.text("Game Over",(300,300),fontsize=100,color="black")
        screen.draw.text("Your score is"+str(score),(500,400),color="blue")

def move_marquee():
    marqueebox.x-=10
    if marqueebox.x<-1000:
        marqueebox.x=1000

def update():
    move_marquee()

def timeup():
    global timer
    if timer:
        timer-=1

def read_question_file():
    global questions
    q_file=open(questionfile,"r")
    for q in q_file:
        questions.append(q)
    q_file.close()

def read_next_question():
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    global score,timer,question
    index=1
    for i in answerboxes:
        if i.collidepoint(pos):
            if index==int(question[5]):
                score+=1
                if questions:
                    question=read_next_question()
                    timer=10
                else:
                    quizover()
            else:
                if questions:
                    question=read_next_question()
                    timer=10
                else:
                    quizover()
    index+=1

def quizover():
    global gameover
    gameover=True

read_question_file()
question = read_next_question()
clock.schedule_interval(timeup,1)
pgzrun.go()