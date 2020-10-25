import turtle as trtl
import time
import random
import win32api
    
sb = trtl.Turtle()
sb.penup()
sb.hideturtle()
sb.setpos(250,250)


score = 0
style = ('Times New Roman', 18, 'italic')

        
def drawing():
    #creates empty list of questions
    questions = []
    #input is true
    inputting = True
    question = input("What term do you want to draw: ")
    questions.append(question)
    #loops until all inputs are done
    while inputting == True:
        if question == 'n':
            inputting = False
            latest = questions.pop()
        else:
            question = input("Whats the next term(if done enter n): ")
            questions.append(question)
    #creates both turtle
    draw = trtl.Turtle()
    end = trtl.Turtle()
    

    end.shape('arrow')
    end.fillcolor('green')
    end.shapesize(4)
    end.penup()
    end.goto(200,-100)
    #happens when clicked and held
    def h2(x,y):
        latest = questions.pop()
        draw.clear()
        draw.penup()
        draw.goto(-350,-350)
        draw.pendown()
        draw.write(latest, font=("Calibri", 20, "bold"))
        draw.penup()
        draw.goto(0,0)
    #detects click
    end.onclick(h2)
    latest = questions.pop()
    draw.penup()
    draw.goto(-350,-350)
    draw.pendown()
    draw.write(latest, font=("Calibri", 20, "bold"))
    draw.penup()
    draw.goto(0,0)

    
    draw.shape('circle')
    draw.shapesize(1)
    draw.speed(0)
    draw.fillcolor('black')
    draw.penup()
    draw.pensize(10)

    #detects dragging
    def dragging(x, y):  # These parameters will be the mouse position
        draw.ondrag(None)
        draw.setheading(draw.towards(x, y))
        draw.goto(x, y)
        draw.stamp()
        draw.ondrag(dragging)


    def h1(x,y):
        draw.goto(x,y)

    draw.ondrag(dragging)
    wn.onclick(h1)

def correct_chosen(x, y):
    global score
    global not_clicked
    score += 1
    not_clicked = False
    sb.clear()
    sb.write(score, style)

bgtrtl = trtl.Turtle()
game1 = trtl.Turtle()
game2 = trtl.Turtle()

game1.shape('square')
game2.shape('square')

game1.fillcolor("cyan")
game2.fillcolor("cyan")

game1.shapesize(7)
game2.shapesize(7)

game1.penup()
game2.penup()

game1.goto(0,20)
game2.goto(0,-140)

trtl.bgcolor('#00ffdf')

count = 0

bgtrtl.speed(0)
bgtrtl.hideturtle()
bgtrtl.penup()
bgtrtl.goto(-160,100)
bgtrtl.write('Tachyphylaxis', font=("Arial", 40, "normal"))

bgtrtl.color('#328CA8')
bgtrtl.penup()
bgtrtl.setpos(270, 410)
bgtrtl.right(45)
bgtrtl.pendown()
bgtrtl.forward(300)
bgtrtl.right(135)
bgtrtl.forward(1000)
bgtrtl.left(135)
bgtrtl.penup()
bgtrtl.setpos(270, -410)
bgtrtl.left(90)
bgtrtl.pendown()
bgtrtl.forward(300)
bgtrtl.right(135)
bgtrtl.forward(1000)
bgtrtl.backward(1000)
bgtrtl.left(135)
bgtrtl.penup()


bgtrtl.penup()
bgtrtl.setpos(-270, 410)
bgtrtl.right(180)
bgtrtl.pendown()
bgtrtl.forward(300)

bgtrtl.penup()
bgtrtl.setpos(-270, -410)
bgtrtl.right(90)
bgtrtl.pendown()
bgtrtl.forward(300)

FONTSIZE = 18
HOLA = 10
FONT = ('Arial', FONTSIZE, 'normal')
HII = ('Arial', HOLA, 'normal')

bgtrtl.penup()
bgtrtl.goto(-150, -200)
bgtrtl.write('By Eric L. Cooper D. Nayan R. Rohan N. Aneesh M.', font=HII)

bgtrtl.goto(-20,15)
bgtrtl.write('Matching')

bgtrtl.goto(-20,0)
bgtrtl.write('Free Draw')


  
    





multiple_choice = False
drawing_game = False
def how1(x,y):
    game1.clear()
    game2.clear()
    bgtrtl.clear()
    game1.hideturtle()
    game2.hideturtle()
    

    trtl.bgcolor("springgreen")
    sb.write(0, style)
    




        

    definitions = []
    answers = []

    writer = trtl.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.speed(0)

    box1 = trtl.Turtle()
    box1.penup()
    box1.shape("square")
    box1.fillcolor("mintcream")
    box1.shapesize(5)
    box1.goto(-200,-100)


    box2 = trtl.Turtle()
    box2.penup()
    box2.shape("square")
    box2.fillcolor("mintcream")
    box2.shapesize(5)
    box2.goto(-73,-100)


    box3 = trtl.Turtle()
    box3.penup()
    box3.shape("square")
    box3.fillcolor("mintcream")
    box3.shapesize(5)
    box3.goto(73,-100)


    box4 = trtl.Turtle()
    box4.penup()
    box4.shape("square")
    box4.fillcolor("mintcream")
    box4.shapesize(5)
    box4.goto(200,-100)
        

    with open('example.txt', 'r') as fin:
        options = int(fin.readline())
        for i in range(options):
            x = fin.readline()
            definitions.append(x)
        
        for j in range(options):
            x = fin.readline()
            answers.append(x)

    for q in answers:

        not_clicked = True
        counter = 0
        options = [definitions[answers.index(q)]]

        for i in range(3):

            x = definitions[random.randint(0,len(answers)-1)]
            while x in options:
                x = definitions[random.randint(0,len(answers)-1)]

            options.append(x)


        random.shuffle(options)
        correct_option = options.index(definitions[answers.index(q)])



        writer.clear()
        writer.goto(-110,0)
        writer.write("What best represents "+q, font = style)
        state_left = win32api.GetKeyState(0x01)

        while counter<5 and not_clicked:    

            writer.goto(-225,-150)
            writer.write(options[0], font = style)
            writer.goto(-100,-150)
            writer.write(options[1], font = style)
            writer.goto(65,-150)
            writer.write(options[2], font = style)
            writer.goto(180,-150)
            writer.write(options[3], font = style)

            time.sleep(2)
            counter += 0
            a = win32api.GetKeyState(0x01)

            if a != state_left: 
                state_left = a
                not_clicked = False

            if correct_option == 0:
                box1.onclick(correct_chosen)
                if not not_clicked:
                    box1.fillcolor("green")
                    box4.fillcolor("red")
                    box2.fillcolor("red")
                    box3.fillcolor("red")

            elif correct_option == 1:
                box2.onclick(correct_chosen)
                if not not_clicked:
                    box2.fillcolor("green")
                    box1.fillcolor("red")
                    box4.fillcolor("red")
                    box3.fillcolor("red")

            elif correct_option == 2:
                box3.onclick(correct_chosen)
                if not not_clicked:
                    box3.fillcolor("green")
                    box1.fillcolor("red")
                    box2.fillcolor("red")
                    box4.fillcolor("red")
                
            elif correct_option == 3:
                box4.onclick(correct_chosen)
                if not not_clicked:
                    box4.fillcolor("green")
                    box1.fillcolor("red")
                    box2.fillcolor("red")
                    box3.fillcolor("red")




        time.sleep(1)
        box1.fillcolor("mintcream")
        box2.fillcolor("mintcream")
        box3.fillcolor("mintcream")
        box4.fillcolor("mintcream")

    writer.clear()
    box1.hideturtle()
    box2.hideturtle()
    box3.hideturtle()
    box4.hideturtle()

    writer.goto(-200,50)
    writer.write("Congratulations!", font=('Times New Roman', 50, 'italic'))
    writer.goto(-90,0)
    writer.write("You got " + str(score) +  " out of " + str(len(definitions)), font=('Times New Roman', 30, 'italic'))


def how2(x,y):
    game1.clear()
    game2.clear()
    bgtrtl.clear()
    game1.hideturtle()
    game2.hideturtle()
    drawing()
    

game2.onclick(how2)
game1.onclick(how1)

game1.write("Multiple Choice")
game2.write("Drawing Game")


wn = trtl.Screen()
wn.mainloop()
