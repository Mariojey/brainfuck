def change_positin_to_right(pos):
    pos+=1
    return pos
def change_position_to_left(pos):
    pos-=1
    return pos
def increment_value(pos):
    tab[pos] += 1
def decrement_value(pos):
    tab[pos]-=1


tab = [0,0,0,0,0,0,0,0,0,0]
actual_pos = 0
while True:
    input_text = input('Write char')
    if input_text == '>':
        actual_pos = change_positin_to_right(actual_pos)
        print(tab)
        print(actual_pos)
    elif input_text == '<':
        actual_pos = change_position_to_left(actual_pos)
        print(tab)
        print(actual_pos)
    elif input_text == '+':
        increment_value(actual_pos)
        print(tab)
    elif input_text == '-':
        decrement_value(actual_pos)
        print(tab)
    else:
        print('Write one of this characters [<,>,+,-]')