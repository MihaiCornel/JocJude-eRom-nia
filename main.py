import turtle
import pandas


screen = turtle.Screen()
screen.title("Jocul judetelor")
image = "da.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("coduri-judete-1.csv")
all_judete = data.judete.to_list()
guess_judete = []


while len(guess_judete) < 42:
    answer_judete = screen.textinput(title=f"{len(guess_judete)}/42 Ghiceste judetul",
                                     prompt="Care este numele unui judet?:").title()
    if answer_judete == "Exit":
        missing_judete = []
        for judete in all_judete:
            if judete not in guess_judete:
                missing_judete.append(judete)
            df = pandas.DataFrame(missing_judete)
            df.to_csv("judete_to_learn.csv")
        print(missing_judete)
        break
    if answer_judete not in guess_judete:
        if answer_judete in all_judete:
            guess_judete.append(answer_judete)
            t1 = turtle.Turtle()
            t1.hideturtle()
            t1.penup()
            judete_data = data[data.judete == answer_judete]
            t1.goto((int(judete_data.x), int(judete_data.y)))
            t1.color("red")
            t1.write(judete_data.judete.item(), align="center", font=("Arial", 10, "normal"))

print("Felicitari, ai terminat jocul!!!")
screen.exitonclick()
