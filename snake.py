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


# & - głowa
# @ - segment ogona
# * - owoc
# # - mur
def print_canvas(canvas, head, tail, fruit):
    '''
    Prints canvas with superimposed fruit, and snake's head & tail
    '''
    # TODO: finish this

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
head = Point(2, 1)
tail = [Point(1, 1), Point(1, 2), Point(1, 3)]
fruit = Point(5, 5)

print_canvas(canvas, head, tail, fruit)


# pkt = Point(4, 11)
# pkt.x
# pkt.y
