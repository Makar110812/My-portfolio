from time import sleep

def indent(lines: int):
    print("\n" * lines, end="")
    return 0

def stopwatch():
    n = 0.0
    while True:
        indent(50)
        print(round(n, 1))
        n += 0.1
        sleep(0.1)

def timer(limit: float):
    while limit > 0:
        indent(50)
        print(round(limit, 1))
        limit -= 0.1
        sleep(0.1)
    indent(50)
    print("Time's up")

def run_stopwatch_or_timer(n: str):
    if n == "" or "0":
        stopwatch()
    else:
        timer(int(n))

print('1    | 1 second',        # Print example of input
      '60   | 1 minute',
      '3600 | 1 hour', sep="\n")

indent(1)

print("How long (in seconds) should the timer be set for? (enter 0 or an empty string for the stopwatch)")
period = input()  # Input value

run_stopwatch_or_timer(period)
