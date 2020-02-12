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

    # Removes string inside quotes
    smaller = input
    for s in inQuotes:
        smaller = smaller.replace(s, "")
    data = smaller.split(" ") # Split by spaces

    # Replaces quotes together with the spaced info from inside the quotes
    index = 0
    for i in range(len(data)):
        if data[i] == "\"\"":
            data[i] = inQuotes[index]
            index += 1

    return data


def print_welcome():

    welcomemsg = """\nThis program searches a database of the London 2012 Olympic gold medalists and the countries they are from. \n\nTo view a list of available commands, type 'help'.\n\nCommands follow the general format of <argument> <argument> <return>, e.g.: \n\n>"Mexico" "swimming" athlete \n\nwill return the list of Mexican athletes who medaled in swimming events.\nTo view this message again, enter 'welcome'. \nTo view the list of acceptable commands, enter 'help'."""

    print(welcomemsg)


# This method prints a list of available commands.
def print_help():
    
    help_msg = "Enter a command in the form of one of these acceptable formats:\n\n" \
               'List discipline                     - Lists all disciplines in the table\n' \
               '"Country" "Discipline" athlete      - Returns athlete(s) from the country and discipline specified. \n' \
               'About "Athlete"                     - Returns the country and event(s) of the athlete specified. \n' \
               '"Athlete" event                     - Returns the event(s) of the given athlete. \n' \
               '"Country" population                - Returns the population of the country specified\n'\
               '"Country" gdp                       - Returns the GDP of the country specified\n'\
               'stop                                - Ends the program\n'\
               '\n'\
               'All arguments should be passed with quotation marks, and names should follow the form of "LASTNAME, Firstname".'

    print(help_msg)


def print_input_error():
    error_msg= "INPUT ERROR. This is not an acceptable command. Enter help for a list of commands." 
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

    
