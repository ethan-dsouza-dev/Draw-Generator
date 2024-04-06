import random
from converters import *
from data import *
import sheet
    
def generate_draw(names, start_time, both_tees):
        
    random.shuffle(names)
    
    num_teams = int(len(names) / 4)
    if len(names) % 4 != 0:
        num_teams += 1
        
    if both_tees:
        half_field = int(len(names) / 2)
        first_tee_draw = generate_draw(names[:half_field], start_time, False)
        tenth_tee_draw = generate_draw(names[half_field:], start_time, False)
        draw = [first_tee_draw, tenth_tee_draw]
    else:
        # initializing draw dictionary
        draw = initialize_dict(start_time, num_teams)
        
        # assign teams to each time
        assign_players(names, draw)
            
    return draw

def assign_players(names, draw):
    try:
        while len(names) != 0:    
            for tee_time in draw.keys():
                draw[f'{tee_time}'].append(names.pop())
    except IndexError as e:
        print("Ran out of players")

def initialize_dict(start_time, num_teams):
    current_time = time_str_to_int(start_time)
    draw = dict()
    
    for team in range(1, num_teams + 1):
            draw[f'{current_time}'] = []
            current_time += 10
    return draw

if __name__ == "__main__":
    print("Starting Now")
    dict_to_pdf(generate_draw(sheet.get_names(), "11:00", False))