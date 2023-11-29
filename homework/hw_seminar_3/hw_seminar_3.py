# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.


board = list(range(1,10))

def draw_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[-3-i*3],'|', board[-2-i*3], '|', board[-1-i*3], '|')
        print('-'*12)

def take_input(revers):
    valid = False
    while not valid:
        player_index = input('Выберите ячейку ' + revers + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Вы уверены, что ввели число?')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = revers
                valid = True
            else:
                print('Ячейка занята.')
        else:
            print('Попробуйте ещё раз.')

def win(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main(board):
    counter =0
    vic = False
    while not vic:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter +=1
        if counter > 4:
            tmp = win(board)
            if tmp:
                print(tmp,'Победа')
                vic = True
                break
            if counter == 9:
                print('Ходы закончились. Ничья!)')
main(board)