# создание матрицы игры:
game_matrix = [[" ",1,2,3 ],
          [1,"-","-","-" ],
          [2,"-","-","-" ],
          [3,"-","-","-" ]]

# функция печати игрового поля:
def make_move():
    for i in range(4):
        for j in range(4):
            print(game_matrix[i][j], end=" ")
        print()

# функции проверки условий выигрыша:
def check_row(row):
    return set(game_matrix[row][1:4]) == ({"X"} or {"O"})

def check_column(col):
    return {game_matrix[1][col], game_matrix[2][col], game_matrix[3][col]} == ({"X"} or {"O"})

def check_diagonals():
    return ({game_matrix[1][1], game_matrix[2][2], game_matrix[3][3]} == ({"X"} or {"O"})) or \
           ({game_matrix[1][3], game_matrix[2][2], game_matrix[3][1]} == ({"X"} or {"O"}))

# печать игрового поля перед началом игры:
make_move()

# ход игры:
while True:
    # ход крестиков и проверка результата хода:
    i = int(input("Введите номер строки для крестика"))
    j = int(input("Введите номер столбца для крестика"))
    game_matrix[i][j] = "X"
    make_move()
    if check_row(i) or check_column(j) or check_diagonals():
        print(check_row(i))
        print("Крестики выиграли")
        break
    elif not any("-" in sub for sub in game_matrix):
        print("Ничья")
        break
    # ход ноликов и проверка результата хода:
    i = int(input("Введите номер строки для нолика"))
    j = int(input("Введите номер столбца для нолика"))
    game_matrix[i][j] = "O"
    make_move()
    if check_row(i) or check_column(j) or check_diagonals():
        print("Нолики выиграли")
        break
    elif not any("-" in sub for sub in game_matrix):
        print("Ничья")
        break