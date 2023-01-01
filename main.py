from tkinter import *
from time import sleep  # NOQA
from random import randint  # NOQA

window = Tk()
window.title("Call of Duty CyberPunk 3000")
size = 30
player_grid = [[size / 2, size / 2 - 1], [size / 2, size / 2 - 2], [size / 2, size / 2 - 3]]
game = Frame(master=window, bg='black')
last_movement = ""
speed = 15
score = 0
checker = 1
score_var = StringVar()


def make_border():
    for up in range(size):  # making the border
        Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=up)
    for down in range(size):  # making the borders
        Label(master=game, bg="grey", width=2, height=1).grid(row=size - 1, column=down)
    for left in range(size):  # making the borders
        Label(master=game, bg="grey", width=2, height=1).grid(row=left, column=0)
    for right in range(size):  # making the borders
        Label(master=game, bg="grey", width=2, height=1).grid(row=right, column=size - 1)


panel = Label(master=window, textvariable=score_var, font=("Ariel", 30, "bold"))
panel.pack(side=TOP)

make_border()
window.update()


def ate_food():
    global food_cord, score  # NOQA
    if player_grid[0] == food_cord:
        score += 1
        score_var.set(f"score : {score}")
        player_snake.update()


def just_ate():
    if player_grid[0] == food_cord:
        return True


def eaten():
    global food_cord  # NOQA
    if player_grid[0] == food_cord:
        ate_food()
        return True


def make_food():
    global food_cord  # NOQA
    food_cord = [randint(1, size - 2), randint(1, size - 2)]
    for pt in player_grid:
        if pt != food_cord:
            food = Label(master=game, bg="#00FF00", width=2, height=1)
            food.grid(row=food_cord[0], column=food_cord[1])
            break
    else:
        food_cord = [randint(1, size - 2), randint(1, size - 2)]
        make_food()


make_food()


def end_game():
    global last_movement, player_grid, score
    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<Left>")
    window.unbind("<Right>")
    end = Label(master=window, text="YOU LOST!", fg="red", bg="black", font=("Ariel", 40, "bold"))
    end.place(x=size * 5, y=size * 10)
    window.update()
    sleep(3)
    end.destroy()
    empty_screen()
    last_movement = "r"
    score_var.set(f"score : {0}")
    score = 0
    player_grid = [[size / 2, size / 2 - 1], [size / 2, size / 2 - 2], [size / 2, size / 2 - 3]]
    player_snake.points = player_grid
    player_snake.update()
    make_border()
    window.update()


class Csnake:
    def __init__(self, map_size, points, frame):
        self.map_size = map_size
        self.points = points
        self.frame = frame

    def update(self):
        window.bind("<Up>", player_snake.move)
        window.bind("<Down>", player_snake.move)
        window.bind("<Right>", player_snake.move)
        window.bind("<Left>", player_snake.move)
        for squares in self.points:
            if squares != self.points[0]:
                Label(master=self.frame, bg="Red", width=2, height=1).grid(row=int(squares[0]), column=int(squares[1]))
            elif squares == self.points[0]:
                Label(master=self.frame, bg="white", width=2, height=1).grid(row=int(self.points[0][0]),
                                                                             column=int(self.points[0][1]))
        window.update()

    def over(self):

        if self.points[0][0] == 0 or self.points[0][1] == 0 or self.points[0][0] == size - 1 or self.points[0][
            1] == size - 1:  # NOQA
            end_game()
        for ps in range(len(self.points)):
            for j in range(len(self.points)):
                if ps != j:
                    if self.points[ps] == self.points[j]:
                        end_game()

    def move(self, event):
        global last_movement, checker
        pressed = event.keysym
        while True:
            if just_ate():
                last_val = (player_grid[len(player_grid) - 1])
                checker = 0
            if eaten():
                make_food()
            self.over()
            empty_screen()

            for point in reversed(range(1, len(self.points))):  # i-1 takes i
                self.points[point] = list(self.points[point - 1])
                if checker == 0:
                    player_grid.append(last_val) # NOQA
                    checker = 1
            ate_food()
            if pressed.lower() == "up":
                if last_movement != 'd':
                    self.points[0][0] = self.points[0][0] - 1
                    last_movement = "u"
                elif last_movement == 'd':
                    last_movement = 'd'
                    self.points[0][0] = self.points[0][0] + 1

            if pressed.lower() == "down":
                if last_movement != "u":
                    self.points[0][0] = self.points[0][0] + 1
                    last_movement = 'd'
                elif last_movement == "u":
                    last_movement = "u"
                    self.points[0][0] = self.points[0][0] - 1

            if pressed.lower() == "right":
                if last_movement != 'l':
                    self.points[0][1] = self.points[0][1] + 1
                    last_movement = 'r'
                elif last_movement == "l":
                    last_movement = "l"
                    self.points[0][1] = self.points[0][1] - 1

            if pressed.lower() == "left":
                if last_movement != "r":
                    self.points[0][1] = self.points[0][1] - 1
                    last_movement = "l"
                elif last_movement == "r":
                    last_movement = 'r'
                    self.points[0][1] = self.points[0][1] + 1

            self.update()
            sleep(1 / speed)


for i in range(size):  # making the map
    if i == 0 or i == size - 1:
        Label(master=game, bg="grey", width=2, height=1).grid(row=i, column=i)
    else:
        Label(master=game, bg="black", width=2, height=1).grid(row=i, column=i)


def empty_screen():
    for nums in player_grid:
        Label(master=game, bg="black", width=2, height=1).grid(row=int(nums[0]), column=int(nums[1]))


player_snake = Csnake(map_size=size, points=player_grid, frame=game)
player_snake.update()

window.bind("<Up>", player_snake.move)
window.bind("<Down>", player_snake.move)
window.bind("<Right>", player_snake.move)
window.bind("<Left>", player_snake.move)

game.pack()
window.mainloop()
