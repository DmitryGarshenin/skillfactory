def printing_desk(list_of_desk):
    for row in list_of_desk:
        for item in row:
            print(item, end=' ')
        print()


def printing_desk_2(desk):
    for i in range(len(desk)+1):
        for j in range(len(desk[i-1])+1):
            if i:
                if j:
                    prt = desk[i-1][j-1]
                else:
                    prt = i
            else:
                prt = j
            print(prt, end=' ')
        print()


def initialization_of_desk(n, m):
    desk = [['-' for j in range(m)] for i in range(n)]
    return desk


def check_win(desk):
    for i in range(len(desk)-2):
        for j in range(len(desk[i])):
            if desk[i][j] != '-':
                if ((desk[i][j] == desk[i+1][j] == desk[i+2][j])
                        or (j < (len(desk[i]) - 2) and (desk[i][j] == desk[i+1][j+1] == desk[i+2][j+2]))
                        or (j < (len(desk[i]) - 2) and (desk[i][j] == desk[i][j+1] == desk[i][j+2]))
                        or (j >= 2 and (desk[i][j] == desk[i+1][j-1] == desk[i+2][j-2]))):
                    return desk[i][j]


print("Добро пожаловать в игру крестики-нолики")
while True:
    try:
        n, m = list(map(int, input("введите размеры поля через пробел: ").split()))
        if n < 3 or m < 3 == 0:
            raise ValueError("значения должны быть не меньше чем 3")
    except Exception as exc:
        print("вы что-то сделали не так: ", exc)
    else:
        print("отлично вы справились! Идем дальше.")
        break

lst = initialization_of_desk(n, m)
print('первыми ходят "крестики"')
name_x = input('введите имя игрока играющего "крестиками" ')
name_o = input('введите имя игрока играющего "ноликами" ')
tuple_names = (name_o, name_x)
tuple_sighs = ('O', 'X')
turn = 1

while (not check_win(lst)) or (turn > n * m):
    printing_desk_2(lst)
    if turn > n * m:
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

# printing_desk_2(lst)
# print(check_win(lst))
# lst[1][0] = 'o'
# lst[2][1] = 'o'
# lst[3][2] = 'o'
# printing_desk_2(lst)
# print(check_win(lst))
