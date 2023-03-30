#job 19
def draw_rectangle(w,h):
    for i in range(h):
        if i == 0 or i == h - 1:
            print('|'+'-' * w+'|')
        else:
            print('|' + ' ' * (w) + '|')
            
draw_rectangle(20,10)
