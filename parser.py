# THis is the file for the Python CLI

def process_data(filename):
    """
    Takes csv file name string as argument, splits columns into separate lists. The zeroth value of each list is the name of the column.
    Returns a 2d list of these lists. Zeroth value is first col, and so on
    """
    f = open(filename, 'r')
    data = f.read()
    f.close()
    data = data.split("\n")
    
    x = len(data)
    y = len(data[0].split(","))
    
    tmp = []
    #separate into array, needs rotating
    for row in data:
        entry = row.split(",")
        tmp.append(entry)
        
    out = []
    titles = []
    #fill titles
    for title in tmp[0]:
        titles.append(title)
    
    #fill data
    for i in range(len(tmp[1])):
        col = []
        for j in range(1, len(tmp)):
            if filename == "summer.csv" and i == 3:
                break
            if filename == "summer.csv" and i==2:
                col.append(tmp[j][i]+","+tmp[j][i+1])
            else:
                col.append(tmp[j][i])
        if col != []:
            out.append(col)
        
    for i in range(len(out)):
        out[i].insert(0,titles[i])
        
    return out

# This method will split a string into an array of strings of keywords and
# variables to be used in SQL queries.
# Accepts: string
# Returns: list
def parse(input):
    split = input.split('\"')
    i = 0
    while i < len(split):
        split[i] = split[i].strip()
        i += 1
    return split


def print_welcome():

    welcomemsg = "\nThis program searches a database of the London 2012 Olympic gold medalists and the countries they are from. \n\nTo view a list of available commands, type 'help'.\n\nCommands follow the general format of <argument> <argument> <return>, e.g.: \n\n>Mexico swimming athlete \n\nwill return the list of Mexican athletes who medaled in swimming events."

    print(welcomemsg)

def print_help():
    
    help_msg = "Enter a command in the form of one of these acceptable formats:\n\n" \
               "List 'Value'                        - Lists all types of value specified\n" \
               "'Country' 'Discipline' athlete      - Returns athletes from the country and discipline specified. \n" \
               "About 'Athlete'                     - Returns information about athlete specified. \n" \
               "'Event' winner                      - Returns the winner for the event specififed. \n" \
               "'Country' population                - Returns the population of the country specified\n"

    print(help_msg) 

    
print_welcome()

print_help()
    
in_use = True

while in_use:
    
    command = input(">")
    
    if command.lower() == "stop":
        in_use = False

    split_command = parse(command)
    print(split_command)
