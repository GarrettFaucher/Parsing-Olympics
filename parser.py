# THis is the file for the Python CLI
import database

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

    return welcomemsg


# This method prints a list of available commands.
def print_help():
    
    help_msg = "Enter a command in the form of one of these acceptable formats:\n\n" \
               'List discipline                     - Lists all disciplines in the table\n' \
               '"Country Abbreviation" "Discipline" athlete      - Returns athlete(s) from the country and discipline specified. \n' \
               'About "Athlete"                     - Returns the country and event(s) of the athlete specified. \n' \
               '"Athlete" event                     - Returns the event(s) of the given athlete. \n' \
               '"Country" population                - Returns the population of the country specified\n'\
               '"Country" gdp                       - Returns the GDP of the country specified\n'\
               'stop                                - Ends the program\n'\
               'load data                           - loads the data\n'\
               '\n'\
               'All arguments should be passed with quotation marks, and names should follow the form of "LASTNAME, Firstname".'

    return help_msg


def print_input_error():
    error_msg= "INPUT ERROR. This is not an acceptable command. Enter help for a list of commands." 
    print(error_msg)

print(print_welcome())

print(print_help())

in_use = True
loaded = False

db = database.Database()

while in_use:
    
    command = input(">")
    output = ""
    
    if command.lower() == "load data":
        db.load_data()
        output = "data loaded."
        loaded = True
    
    elif command.lower() == "stop":
        in_use = False
        output = "halting..."
        
    elif command.lower() == "welcome":
        output = print_welcome()
    
    elif command.lower() == "help":
        output = print_help()

    else:
        if not loaded:
            db.load_data()
            loaded = True
        split_command = parse(command)
        output = db.parsed_to_sql(split_command)
        
    print(output)
