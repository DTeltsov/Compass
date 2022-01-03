
def check(facing, turn):
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']    
    if type(turn) != int:
        return 'not a number'
    if turn > 1080 or turn < -1080:
        return 'more than 1080 or less than -1080'
    if facing not in compass:
        return 'Not sign of compass'
    if turn % 45 != 0:
        return 'not a multiple of 45'
        

def direction(facing, turn):
    #сначала проверим входные данные
    flag = check(facing,turn)
    if flag:
        return flag
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    #уберём лишние круги
    if abs(turn) > 360:
            turn = turn - 360 * (turn // 360)
    turn = turn / 45
    element = compass.index(facing) + 1
    #перейдём в начало списка, если конечный индекс выходит больше, чем длинна списка
    if element + turn > len(compass):
        element = int(((element + turn) - len(compass)) - 1)
    else:
        element = int((element + turn) - 1)
    res = compass[element]
    return res 


def main():
    print(direction('NE', 45))

if __name__ == '__main__':
    main()