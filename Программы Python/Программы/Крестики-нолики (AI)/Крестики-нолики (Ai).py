# Создаем пустое поле для игры
board = [' ' for _ in range(1, 11)]

# Функция для отображения игрового поля
def display_board():
    print('-------------')
    print('|', board[1], '|', board[2], '|', board[3], '|')
    print('-------------')
    print('|', board[4], '|', board[5], '|', board[6], '|')
    print('-------------')
    print('|', board[7], '|', board[8], '|', board[9], '|')
    print('-------------')

# Функция для проверки победителя
def check_winner():
    # Все возможные выигрышные комбинации
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    
    return False

# Функция для выполнения хода игрока
def make_move(player):
    while True:
        position = int(input(player, ', выберите позицию (1-9) :'))
        if 1 <= position <= 9 and board[position] == ' ':
            board[position] = player
            break
        else:
            print('Некорректный ход. Попробуйте еще раз.')

# Основной игровой цикл
def play_game():
    player = 'X'
    n = 0
    
    while True:
        display_board()
        make_move(player)
        n = n + 1
        
        if check_winner():
            display_board()
            print('Игрок', player, 'победил!')
            break
        
        if n == 9:
            display_board()
            print('Ничья!')
            break
        
        player = 'O' if player == 'X' else 'X'

# Запускаем игру
play_game()
