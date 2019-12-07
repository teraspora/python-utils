# © John Lynch 2019-05-15

position = (0, 0)
direction = (0, 1)
instructions = 'L++ R-- L+'  # Example 2

def turn_left():
    global direction
    (x, y) = direction
    direction = (-y, x)

def turn_right():
    global direction
    (x, y) = direction
    direction = (y, -x)

def move(distance):
    global position, direction
    (x, y) = position
    (xd, yd) = direction
    position = (x + xd * distance, y + yd * distance)

def travel(input):
    for symbol in input:
        if symbol == '+':
            move(1)
        elif symbol == '-':
            move(-1)
        elif symbol == 'L':
            turn_left()
        elif symbol == 'R':
            turn_right()
        else:
            pass

travel(instructions)
print(f'You ended up at coordinates {position}!')
