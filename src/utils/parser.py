def parser(address):
    result = ""
    with open (address,"r")as file:
        result = file.read()

    return result