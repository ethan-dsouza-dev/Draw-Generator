import random
import datetime
from converters import *
from data import *
    
def generate_draw(names, start_time):
    current_time = time_str_to_int(start_time)
    print(current_time)
    random.shuffle(names)
    draw = dict()
    
    if len(names) % 4 == 0:
        num_teams = int(len(names) / 4)
    else:
        num_teams = int(len(names) / 4) + 1
        
    # initializing dictionary
    for team in range(1, num_teams + 1):
            draw[f'{current_time}'] = []
            current_time += 10
    print(draw)
    
    # assign teams to each time
    current_time = time_str_to_int(start_time)
    try:
        while len(names) != 0:    
            for team in draw.keys():
                draw[f'{current_time}'].append(names.pop())
                current_time += 10
            current_time = time_str_to_int(start_time)
    except IndexError as e:
        print("Ran out of players")
        return draw
            
    return draw

print(generate_draw(names, "11:00"))