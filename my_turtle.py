import turtle


class MyTurtle(turtle.Turtle):
    def __init__(self, width, height, *args, **kwargs):
        screen = turtle.Screen()
        screen.bgcolor("#FADA5E")

        super().__init__(*args, **kwargs)

    def exit_on_click(self):

        turtle.exitonclick()

