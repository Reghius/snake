import random
from turtle import right

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_canvas(n, m, wall_sign=1):
    '''
    Creates a `n` by `m` playable area, with walls surrounding it
    '''

    canvas = []

    for i in range(n):
        column = []
        for j in range(m):
            if j <= m and i == 0 or \
               j <= m and i == n-1 or \
               j == 0 or \
               j == m-1:
                column.append(1)
            else:
                column.append(0)
        canvas.append(column)

    return canvas

def print_canvas(canvas, head, tail, fruit):
    '''
    Prints canvas with superimposed fruit, and snake's head & tail
    '''
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            if head.x == i and head.y == j:
                print('&', end='')
            elif fruit.x == i and fruit.y == j:
                print('*', end='')
            elif canvas[i][j] == 1:
                print('#', end='')
            else:
                for segment in tail:
                    if segment.x == i and segment.y == j:
                        print('@', end='')
                        break
                else:
                    print(' ', end='')
        print()

canvas = create_canvas(10, 20)

def snake_movement():
    head_position = input('To which direction you want to move the head? ')
    if head_position == 'left':
        for i in range(len(tail)-1, -1, -1):
            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        tail[0].x = head.x
        tail[0].y = head.y
        head.y -= 1
    elif head_position == 'right':
        for i in range(len(tail)-1, -1, -1):
            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        tail[0].x = head.x
        tail[0].y = head.y
        head.y += 1
    elif head_position == 'up':
        for i in range(len(tail)-1, -1, -1):
            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        tail[0].x = head.x
        tail[0].y = head.y
        head.x -= 1
    elif head_position == 'down':
        for i in range(len(tail)-1, -1, -1):
            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        tail[0].x = head.x
        tail[0].y = head.y
        head.x += 1

def snake_eating():
    if head.x == fruit.x and head.y == fruit.y:
        tail.append(Point(tail[-1].x, tail[-1].y))
        fruit.x = random.randint(1, 8)
        fruit.y = random.randint(1, 19)
    for i in range(len(tail)):
        if fruit.x == tail[i].x and fruit.y == tail[i].y or fruit.x == head.x and fruit.y == head.y:
            fruit.x = random.randint(1, 8)
            fruit.y = random.randint(1, 19)

def game_logic():
    # snake collsion
    if head.x == 0 or head.x == 9 or head.y == 0 or head.y == 19:
        print('You lost!')
    for i in range(len(tail)):
        if head.x == tail[i].x and head.y == tail[i].y:
            print('You lost!')

if __name__ == '__main__':
    head = Point(2, 1)
    tail = [Point(1, 1), Point(1, 2), Point(1, 3)]
    fruit = Point(5, 5)

    while True:
        print_canvas(canvas, head, tail, fruit)
        snake_movement()
        snake_eating()
        game_end = game_logic()
        if game_end:
            break

# & - głowa
# @ - segment ogona
# * - owoc
# # - mur