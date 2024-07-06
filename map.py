# X and Y
# 5x6
easy = [
    [0,0,7,0,0],
    [0,7,1,7,0],
    [0,7,0,7,0],
    [0,7,0,7,0],
    [0,8,7,0,0],
    [0,0,0,0,0]
]

# 11x10
medium = [
    [0,7,0,0,0,0,0,0,0,0,0],
    [0,7,0,7,0,7,0,0,0,7,0],
    [0,7,7,7,7,7,7,7,7,7,0],
    [0,7,0,7,0,7,0,7,0,7,0],
    [0,7,7,0,7,0,7,7,7,7,0],
    [0,7,0,0,7,7,7,0,7,7,0],
    [0,7,0,0,7,0,0,0,0,7,0],
    [0,7,7,0,7,8,7,7,7,7,0],
    [0,0,7,7,7,0,0,0,7,0,0],
    [0,0,0,0,0,0,0,0,0,0,0]
]

# 15x14
hard = [
    [0,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,7,7,7,7,7,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,7,7,7,7,7,7,7,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,7,7,7,0,7,7,7,0],
    [0,0,0,0,0,0,7,0,0,7,0,7,0,7,0],
    [0,7,7,7,7,7,7,0,0,7,0,7,0,7,0],
    [0,7,0,0,7,0,7,7,7,7,0,7,0,7,0],
    [0,7,7,7,7,0,7,0,0,0,7,7,0,7,0],
    [0,7,0,0,7,0,7,7,7,7,7,0,0,7,0],
    [0,7,7,8,7,7,7,0,7,0,7,7,7,7,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

# 18x20
god = [
    [0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0],
    [0,7,7,0,7,0,0,7,7,7,7,7,7,7,0,0,7,0],
    [0,0,7,0,7,0,0,0,0,0,7,0,0,0,7,0,7,0],
    [0,7,7,7,7,7,7,7,7,7,7,7,7,0,7,0,7,0],
    [0,7,0,7,0,0,7,0,0,0,0,0,7,0,7,7,7,0],
    [0,7,0,0,7,7,7,0,7,7,7,0,7,0,0,7,0,0],
    [0,7,0,7,7,0,7,7,7,0,0,0,7,0,0,7,0,0],
    [0,7,0,0,0,0,0,0,0,0,0,0,7,0,0,7,0,0],
    [0,7,0,0,7,7,7,7,7,7,7,7,7,0,0,7,0,0],
    [0,7,0,0,7,0,0,0,7,0,0,0,0,7,7,7,0,0],
    [0,7,0,0,7,0,0,0,7,0,0,7,0,0,0,7,7,0],
    [0,7,0,0,7,0,0,7,7,7,7,7,7,0,0,0,0,0],
    [0,7,0,0,7,0,0,7,0,0,7,0,7,0,0,7,7,0],
    [0,7,7,7,7,7,7,7,0,0,0,0,7,0,0,7,0,0],
    [0,7,0,0,0,0,0,7,0,0,7,0,7,7,7,7,0,0],
    [0,7,0,0,0,0,0,7,0,0,7,7,7,0,7,0,0,0],
    [0,7,0,0,7,0,0,7,0,0,7,0,7,7,7,7,0,0],
    [0,7,0,0,7,0,7,7,7,7,0,0,0,0,0,7,0,0],
    [0,7,7,7,7,0,7,0,0,7,7,8,7,7,7,7,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

# si maam bahala dito
'''custom = [
    [0,0,0,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,7,7,7,7,7,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,7,7,7,7,7,7,7,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,7,7,7,0,7,0,7,0],
    [0,0,0,0,0,0,7,0,0,7,0,7,0,7,0],
    [0,7,7,7,7,7,7,7,0,7,0,7,0,7,0],
    [0,7,0,0,7,0,0,7,7,7,0,7,0,7,0],
    [0,7,7,7,7,0,0,7,0,0,0,7,0,7,0],
    [0,7,0,0,7,7,0,7,7,7,7,7,0,7,0],
    [0,7,0,0,0,7,0,8,0,0,0,7,0,7,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]'''

# si maam bahala dito
custom = [
    [0,0,0,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,7,7,7,7,7,0,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,7,7,7,7,7,7,7,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,0,0,0,0,7,0,7,0],
    [0,0,7,0,0,0,7,7,7,7,0,7,0,7,0],
    [0,0,0,0,0,0,7,0,0,7,0,7,0,7,0],
    [0,7,7,7,7,7,7,7,0,7,0,7,0,7,0],
    [0,7,0,0,7,0,0,7,7,7,0,7,0,7,0],
    [0,7,7,7,7,0,0,7,0,0,0,7,0,7,0],
    [0,7,0,0,7,7,0,7,7,7,7,7,0,7,0],
    [0,7,0,0,0,7,0,8,0,0,0,7,0,7,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def calc_custom(screen_width, screen_height):
    fog_size = None
    tile_size = None
    y = len(custom)
    x = len(custom[0])
    print(x,y)
    xy_pos = {
        
    }

    return fog_size, tile_size, xy_pos

    '''if len(custom) <=3:
        return 38, 38
    elif len(custom) <=10:
        print(10)
        return 34, 34
    elif len(custom) <=14:
        print(14)
        return 30, 25
    elif len(custom) <=20:
        print(20)
        return 20, 22
    elif len(custom) <=25:
        return 16, 16
    elif len(custom) <=30:
        return 10, 10
    else:
        return 0, 0'''
    