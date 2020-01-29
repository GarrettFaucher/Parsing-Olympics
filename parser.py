# THis is the file for the Python CLI


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
    
print_welcome()
