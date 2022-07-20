print('Добро пожаловать в мини-игру "Крестики-нолики"!') #приветствие
begin_field = ['', '1', '2', '3', '\n', '4', '5', '6', '\n', '7', '8', '9'] #начальное поле, матрица
print('Игровое поле:')
print(*begin_field)

print('Время игрокам представиться!')
player_1 = input('Игрок №1, напишите Ваше имя: ') #вводим переменную с именами игроков
player_2 = input('Игрок №2, напишите Ваше имя: ') #вводим переменную с именами игроков
print(f'Ну что ж, {player_1}, {player_2}, теперь пришло время определиться с вашим символом в игре!')
print(f'{player_1}, выберете ваш символ...')
player_1_symb = input('X или 0?' '\n') #вводим переменную с символом игрока №1
if player_1_symb == 'X':
    print(f'{player_1}, ваш символ в игре "Крестики-нолики" - X')
else:
    print(f'{player_2}, ваш символ в игре "Крестики-нолики" - 0')
print(f'{player_2}, выберете ваш символ...')
player_2_symb = input('X или 0?' '\n') #вводим переменную с символом игрока №2
if player_2_symb == 'X':
    print(f'{player_2}, ваш символ в игре "Крестики-нолики" - X')
else:
    print(f'{player_2}, ваш символ в игре "Крестики-нолики" - 0')
print(f'Начнем игру! \n{player_1}, ваш ход...')
print(*begin_field)

while True:
        player_1_step = input(f'{player_1}, выберете номер клетки куда вы хотите сходить...')
        if player_1_step in begin_field:
            for index, item in enumerate(begin_field):
                if any([all([begin_field[1:4] == ['X', 'X', 'X']]), #варианты побед 1 игрока
                        all([begin_field[5:8] == ['X', 'X', 'X']]),
                        all([begin_field[9:12] == ['X', 'X', 'X']]),
                        all([begin_field[1] == 'X',
                             begin_field[5] == 'X',
                             begin_field[9] == 'X']),
                        all([begin_field[2] == 'X',
                             begin_field[6] == 'X',
                             begin_field[10] == 'X']),
                        all([begin_field[3] == 'X',
                             begin_field[7] == 'X',
                             begin_field[11] == 'X']),
                        all([begin_field[1] == 'X',
                             begin_field[6] == 'X',
                             begin_field[11] == 'X']),
                        all([begin_field[3] == 'X',
                             begin_field[6] == 'X',
                             begin_field[9] == 'X'])]):
                    print(f'Игрок {player_1} победил! \n Конец игры!')
                    break
                elif item == player_1_step: #ходы игрока 1
                    begin_field[index] = 'X'
        print(*begin_field)
        player_2_step = input(f'{player_2}, выберете номер клетки куда вы хотите сходить...')
        if player_2_step in begin_field:
            for index, item in enumerate(begin_field):
                if any([all([begin_field[1:4] == ['0', '0', '0']]), #варианты побед 2 игрока
                        all([begin_field[5:8] == ['0', '0', '0']]),
                        all([begin_field[9:12] == ['0', '0', '0']]),
                        all([begin_field[1] == '0',
                             begin_field[5] == '0',
                             begin_field[9] == '0']),
                        all([begin_field[2] == '0',
                             begin_field[6] == '0',
                             begin_field[10] == '0']),
                        all([begin_field[3] == '0',
                             begin_field[7] == '0',
                             begin_field[11] == '0']),
                        all([begin_field[1] == '0',
                             begin_field[6] == '0',
                             begin_field[11] == '0']),
                        all([begin_field[3] == '0',
                             begin_field[6] == '0',
                             begin_field[9] == '0'])]):
                    print(f'Игрок {player_2} победил! \n Конец игры!')
                    break
                elif item == player_2_step: #ходы 2 игрока
                    begin_field[index] = '0'
        print(*begin_field)
