#job23

def draw_triangle(h):
    for i in range(h):
       for i in range(h):
        if i == 0:
            print(' ' * (h - i - 1) + '/\\')
        elif i == h - 1:
            print('/' + '_' * (2 * h - 2) + '\\')
        else:
            print(' ' * (h - i - 1) + '/' + ' ' * (2 * i) +'\\')

draw_triangle(5)