# Крестики нолики
from tkinter import *


def two_player():
    global x, sp, maps, root
    sp = ['X', '0', 'X', '0', 'X', '0', 'X', '0', 'X', '0']
    x = 0
    # Инициализация карты
    maps = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]  # Инициализация пустыми значениями

    # Инициализация победных линий
    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

    # Получить текущий результат игры
    def get_result():
        global button
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                print("X")
                Label(window, text='Победил первый игрок X', width=20, font=('Time Nem Roman', 12, 'bold')).place(x=50,
                                                                                                                  y=10)
                for button in buttons:
                    button.config(state="disabled")
            if maps[i[0]] == "0" and maps[i[1]] == "0" and maps[i[2]] == "0":
                print("0")
                Label(window, text='Победил второй игрок 0', width=20, font=('Time Nem Roman', 12, 'bold')).place(x=50,
                                                                                                                  y=10)
                for button in buttons:
                    button.config(state="disabled")

    def butt(button_index):

        global x, sp, maps
        x += 1

        if x <= len(sp):
            button_text = sp[x - 1]
        else:
            button_text = ""
        # Отключение кнопки перед изменением
        buttons[button_index].config(state="disabled")
        Label(root, text=button_text, width=2, height=1, font=('Time New Roman', 45, 'bold'), bg='white').place(
            x=coord[button_index][0], y=coord[button_index][1])

        maps[button_index] = button_text  # Используйте button_index вместо i
        get_result()

    root = Frame(window, bg='black', width=246, height=238, bd=0)
    root.place(x=30, y=50)

    buttons = []
    coord = []

    for row in range(3):
        for col in range(3):
            button_index = row * 3 + col
            button = Button(root, width=3, height=1, bd=0, font=('Arial', 30, 'bold'), bg='white',
                            command=lambda i=button_index: butt(i))
            button.place(x=col * 85, y=row * 80)
            coord.append([col * 85, row * 80])
            buttons.append(button)


window = Tk()
window.geometry('306x352')
window.configure(bg='grey')

Button(window, text='Повторить', bg='green', bd=0, font=('Arial', 10, 'bold'), command=two_player).place(x=115, y=310)

window.mainloop()
