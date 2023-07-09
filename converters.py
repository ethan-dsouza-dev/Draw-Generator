import re

#converts a time in a string formatted as ##:## to a 4 digit int ####
def time_str_to_int(time_str):
    time_pattern = re.compile('\d\d')
    matches = re.findall(time_pattern, time_str)
    time_int = ''
    for match in matches:
        time_int += match
        
    return int(time_int)

print(time_str_to_int("11:00"))