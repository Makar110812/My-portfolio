def enter_int():
    enter_int = int(input('Введите число для запуска таймера (2000 ≈ 1 секунда): '))
    return enter_int
def timer(enter_int):
    for n in range(enter_int + 1):
        if n != 0:
            print(n)
def finish():
    print('FINISH')
def start():
    timer(enter_int())
    finish()

start()
