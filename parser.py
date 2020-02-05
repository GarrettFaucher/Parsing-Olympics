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

    # Finds the string inside of the quotes
    countS = -1
    countE = 0
    lastE = 0
    start = False
    inQuotes = []
    for i in range(len(input)):
        if (input[i] == "\""):
            if countS == -1:
                countS = i+1
            else:
                countE = i
                lastE = i
                inQuotes.append(input[countS:countE])
                countS = -1
                countE = 0

    print(inQuotes)
    # Removes string inside quotes
    smaller = input
    for s in inQuotes:
        smaller = smaller.replace(s, "")
        print(smaller)
    data = smaller.split(" ") # Split by spaces
    print(data)

    # Replaces quotes together with the spaced info from inside the quotes
    index = 0
    for i in range(len(data)):
        if data[i] == "\"\"":
            data[i] = inQuotes[index]
            index += 1

    return data

# This method will take a parsed list and reorganise the order and convert
# keywords to table names.
# Accepts: parsed list
# Returns: list with converted names from english
def converter(input):
    data = []

    for i in range(len(input)):
        if (input[i] == "country" or input[i] == "Country" or input[i] == "COUNTRY"):
            data[i] = "fldCountry"
        elif (input[i] == "population" or input[i] == "Population" or input[i] == "population"):
            data[i] = "fldPopulation"
        elif (input[i] == "gdp" or input[i] == "Gdp" or input[i] == "GDP"):
            data[i] = "fldGDP"
        elif (input[i] == "sport" or input[i] == "Sport" or input[i] == "SPORT"):
            data[i] = "fldSport"
        elif (input[i] == "discipline" or input[i] == "Discipline" or input[i] == "DISCIPLINE"):
            data[i] = "fldDiscipline"
        elif (input[i] == "athlete" or input[i] == "Athlete" or input[i] == "ATHLETE"):
            data[i] = "fldAthlete"
        elif (input[i] == "gender" or input[i] == "Gender" or input[i] == "GENDER"):
            data[i] = "fldGender"
        elif (input[i] == "event" or input[i] == "Event" or input[i] == "EVENT"):
            data[i] = "fldEvent"
        else:
            data[i] = input[i]

    print(data)
    return data


def print_welcome():

    welcomemsg = "\nThis program searches a database of the London 2012 Olympic gold medalists and the countries they are from. \n\nTo view a list of available commands, type 'help'.\n\nCommands follow the general format of <argument> <argument> <return>, e.g.: \n\n>'Mexico' 'swimming' athlete \n\nwill return the list of Mexican athletes who medaled in swimming events.\nTo view this message again, enter 'welcome'. \nTo view the list of acceptable commands, enter 'help'."

    print(welcomemsg)

# This method prints a list of available commands.
def print_help():
    
    help_msg = "Enter a command in the form of one of these acceptable formats:\n\n" \
               "List 'Value'                        - Lists all types of value specified\n" \
               "'Country' 'Discipline' athlete      - Returns athletes from the country and discipline specified. \n" \
               "About 'Athlete'                     - Returns information about athlete specified. \n" \
               "'Event' winner                      - Returns the winner for the event specififed. \n" \
               "'Country' population                - Returns the population of the country specified\n"

    print(help_msg)

def print_input_error(error):
    error_msg= "INPUT ERROR.  " + error + " Is not a valid query \n type 'help' to view a list of available commands\n"
    print(error_msg)


print_welcome()

print_help()

in_use = True

while in_use:
    
    command = input(">")
    
    if command.lower() == "stop":
        in_use = False
        
    if command.lower() == "welcome":
        print_welcome()
    
    if command.lower() == "help":
        print_help()

    split_command = parse(command)
    print(split_command)

    
