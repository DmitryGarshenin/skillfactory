def printing_desk_2(desk):
    """функция для вывода поля (списка) и координат"""
    for i in range(len(desk)+1):
        for j in range(len(desk[i-1])+1):
            if i:
                if j:
                    prt = desk[i-1][j-1]
                else:
                    prt = i  # вывод координатной сетки
            else:
                prt = j  # вывод координатной сетки
            print(prt, end=' ')
        print()


def initialization_of_desk(rows, colomns):
    """ создание двумерного массива (списка списков) необходимого размера"""
    desk = [['-' for i in range(colomns)] for j in range(rows)]
    return desk


def check_win(desk):
    """ функция проверки на наличие победителя"""
    for i in range(len(desk)-2):
        for j in range(len(desk[i])):
            if desk[i][j] != '-':
                if ((desk[i][j] == desk[i+1][j] == desk[i+2][j])
                        or (j < (len(desk[i]) - 2) and (desk[i][j] == desk[i+1][j+1] == desk[i+2][j+2]))
                        or (j < (len(desk[i]) - 2) and (desk[i][j] == desk[i][j+1] == desk[i][j+2]))
                        or (j >= 2 and (desk[i][j] == desk[i+1][j-1] == desk[i+2][j-2]))):
                    return desk[i][j]


print("Добро пожаловать в игру крестики-нолики")
# ввод размеров поля
while True:
    try:
        length, hight = list(map(int, input("введите размеры поля через пробел (формат: длинна высота): ").split()))
        if length < 3 or hight < 3 == 0:
            raise ValueError("значения должны быть не меньше чем 3")
    except Exception as exc:
        print("вы что-то сделали не так: ", exc)
    else:
        print("отлично вы справились! Идем дальше.")
        break

# начальные установки, ввод имен
lst = initialization_of_desk(hight, length)
print('первыми ходят "крестики"')
name_x = input('введите имя игрока играющего "крестиками" ')
name_o = input('введите имя игрока играющего "ноликами" ')
tuple_names = (name_o, name_x)  # кортеж для хранения имен игроков
tuple_sighs = ('O', 'X')  # кортеж для хранения знаков соответствующих игроков
turn = 1

# цикл игры
while not check_win(lst):
    printing_desk_2(lst)
    if turn > length * hight:
        print("У вас ничья, поля закончились!!!")
        break
    try:
        print(f"ход игрока {tuple_names[turn % 2]}, играющего {tuple_sighs[turn % 2]}")
        x, y = list(map(int, input("введите координаты поля через пробел (x y): ").split()))
        if lst[y-1][x-1] != '-':
            raise ValueError("поле уже занято")
        lst[y-1][x-1] = tuple_sighs[turn % 2]
    except Exception as exc:
        print("вы что-то сделали не так: ", exc)
        input("пожалуйста, нажмите ENTER для продолжения")
    else:
        print("отличный ход!")
        turn += 1
else:
    printing_desk_2(lst)
    print(f"после {turn - 1} ходов победил игрок {tuple_names[(turn - 1) % 2]}! Поздравляем!!!")
