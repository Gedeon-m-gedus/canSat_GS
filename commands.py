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

def check_commands(cmd):
    commands = cleanCommands()
    comms = []
    if len(cmd)<1:
        return False,cmd
    
    for com in commands.values():
        for c in com:
            if len(c)>3:
                comms += c.split(' ')
                if cmd in c.split(' '):
                    return True,c.split(' ')[-1]
    return False,cmd

def run_command(cmd):
    flg,cm = check_commands(cmd)
    if flg:
        print('Valid command', cm)
    else:
        print('Invalid command',cm)
# import os
# print(os.getcwd())