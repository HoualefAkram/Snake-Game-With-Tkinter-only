from tkinter import *
from time import sleep  # NOQA
from random import randint  # NOQA

window = Tk()
window.title("Call of Duty CyberPunk 3000")
size = 30
player_grid = [[size / 2, size / 2 - 1], [size / 2, size / 2 - 2], [size / 2, size / 2 - 3]]
game = Frame(master=window, bg='black')
last_movement = ""
speed = 20
score = -1
score_var = StringVar()

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

window.update()

last_food = [0, 0]
food_cord = player_grid[0]


def make_food():
    global food_cord, last_food, score, speed  # NOQA
    if player_grid[0] == food_cord:
        score += 1
        score_var.set(f"score : {score}")
        food_cord = [randint(1, size - 2), randint(1, size - 2)]
        # speed **= 2   more speed  if you want
        for pt in player_grid:
            if pt != food_cord and food_cord != last_food:
                food = Label(master=game, bg="#00FF00", width=2, height=1)
                food.grid(row=food_cord[0], column=food_cord[1])
                last_food = food_cord
                player_grid.append([0, 0])

                break
        else:
            food_cord = [randint(1, size - 2), randint(1, size - 2)]
            make_food()


def end_game():
    global last_movement, player_grid, score, speed
    for nums in player_grid:
        Label(master=game, bg="black", width=2, height=1).grid(row=int(nums[0]), column=int(nums[1]))
    end = Label(master=window, text="YOU LOST!", fg="red", bg="black", font=("Ariel", 40, "bold"))
    end.place(x=size * 5, y=size * 10)
    window.update()
    sleep(3)
    end.destroy()
    Label(master=game, bg="black", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                           column=int(player_grid[-1][1]))  # empty_map()
    Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=0)
    last_movement = "r"
    score_var.set(f"score : {0}")
    score = 0
    player_grid = [[size / 2, size / 2 - 1], [size / 2, size / 2 - 2], [size / 2, size / 2 - 3],
                   [size / 2, size / 2 - 4]]
    update()
    # make border
    for up in range(size):  # making the border # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=up)
    for down in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=size - 1, column=down)
    for left in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=left, column=0)
    for right in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=right, column=size - 1)

    window.update()


def update():
    for squares in player_grid:
        if squares != player_grid[0]:
            Label(master=game, bg="Red", width=2, height=1).grid(row=int(squares[0]), column=int(squares[1]))
        elif squares == player_grid[0]:
            Label(master=game, bg="white", width=2, height=1, relief=SUNKEN, bd=2).grid(
                row=int(player_grid[0][0]),
                column=int(player_grid[0][1]))
    window.update()


def move(event):
    global last_movement
    pressed = event.keysym
    while True:
        make_food()

        if player_grid[0][0] == 0 or player_grid[0][1] == 0 or player_grid[0][0] == size - 1 or player_grid[0][
            # over()
            1] == size - 1:  # NOQA
            end_game()
        for ps in range(len(player_grid)):
            for j in range(len(player_grid)):
                if ps != j:
                    try:
                        if player_grid[ps] == player_grid[j]:
                            end_game()
                    except IndexError:
                        pass

        Label(master=game, bg="black", width=2, height=1).grid(row=int(player_grid[-1][0]),  # empty_map()
                                                               column=int(player_grid[-1][1]))
        Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=0)

        for point in reversed(range(1, len(player_grid))):  # i-1 takes i
            player_grid[point] = list(player_grid[point - 1])

        if pressed.lower() == "up":
            if last_movement != 'd':
                player_grid[0][0] = player_grid[0][0] - 1
                last_movement = "u"
            elif last_movement == 'd':
                last_movement = 'd'
                player_grid[0][0] = player_grid[0][0] + 1

        if pressed.lower() == "down":
            if last_movement != "u":
                player_grid[0][0] = player_grid[0][0] + 1
                last_movement = 'd'
            elif last_movement == "u":
                last_movement = "u"
                player_grid[0][0] = player_grid[0][0] - 1

        if pressed.lower() == "right":
            if last_movement != 'l':
                player_grid[0][1] = player_grid[0][1] + 1
                last_movement = 'r'
            elif last_movement == "l":
                last_movement = "l"
                player_grid[0][1] = player_grid[0][1] - 1

        if pressed.lower() == "left":
            if last_movement != "r":
                player_grid[0][1] = player_grid[0][1] - 1
                last_movement = "l"
            elif last_movement == "r":
                last_movement = 'r'
                player_grid[0][1] = player_grid[0][1] + 1

        update()
        sleep(1 / speed)


for i in range(size):  # making the map
    if i == 0 or i == size - 1:
        Label(master=game, bg="grey", width=2, height=1).grid(row=i, column=i)
    else:
        Label(master=game, bg="black", width=2, height=1).grid(row=i, column=i)

update()

window.bind("<Up>", move)
window.bind("<Down>", move)
window.bind("<Right>", move)
window.bind("<Left>", move)

game.pack()
window.mainloop()
