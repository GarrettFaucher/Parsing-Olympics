# THis is the file for the Python CLI

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

    
