def valid_input(inp):
    try:
        if not inp.lower() == 'y' or inp.lower() == 'n' or inp.lower() == 'yes' or inp.lower() == 'no':
            print ("Incorrect input. Try again")
            return None
        return inp
    except:
        print ("Incorrect input. Try again")
        return None
