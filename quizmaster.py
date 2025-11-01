import pgzrun

WIDTH = 1000
HEIGHT = 600

timer=10

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
    screen.draw.filled_rect(questionbox,"blue")
    for i in answerboxes:
        screen.draw.filled_rect(i,"green")
    screen.draw.filled_rect(timerbox,"yellow")
    screen.draw.textbox(str(timer),timerbox,color="red")
    screen.draw.filled_rect(scorebox,"yellow")
    screen.draw.filled_rect(skipbox,"orange")

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

clock.schedule_interval(timeup,1)
pgzrun.go()