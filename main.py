import random
import datetime
from converters import *
from data import *
    
def generate_draw(names, start_time, *both_tees):
    if both_tees == None:
        both_tees == False
        
    random.shuffle(names)
    draw = dict()
    
    num_teams = int(len(names) / 4)
    if len(names) % 4 != 0:
        num_teams += 1
        
    # initializing draw dictionary
    initialize_dict(time_str_to_int(start_time), draw, num_teams)
    
    # assign teams to each time
    assign_players(names, start_time, draw)
            
    return draw

def assign_players(names, start_time, draw):
    current_time = time_str_to_int(start_time)
    try:
        while len(names) != 0:    
            for team in draw.keys():
                draw[f'{current_time}'].append(names.pop())
                current_time += 10
            current_time = time_str_to_int(start_time)
    except IndexError as e:
        print("Ran out of players")

def initialize_dict(current_time, draw, num_teams):
    for team in range(1, num_teams + 1):
            draw[f'{current_time}'] = []
            current_time += 10
    print(draw)

print(generate_draw(names, "11:00", False))