def cleanCommands(path='./files/commands/can_sat_ground_station_command.txt'):
    with open(path) as f:
        commands_file = f.readlines()
    commands = listToString(commands_file).split('!!!')
    commands.pop(0)
    command_dict = {}
    for i,c in enumerate(commands):
        cc = c.split('\n')
        command_dict[cc[i]] = cc[1:]
    return command_dict
    
def listToString(s):   
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1 