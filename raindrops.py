def convert(number):

    #git init
    #git remote add origin https://github.com/Redzyk/exercism_raindrops.git

    result = ""

    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        result += "PlingPlangPlong"

    elif number % 3 == 0 and number % 5 == 0:
        result += "PlingPlang"

    elif number % 3 == 0 and number % 7 == 0:
        result += "PlingPlong"

    elif number % 5 == 0 and number % 7 == 0:
        result += "PlangPlong"

    elif number % 3 == 0:
        result += "Pling"

    elif number % 5 == 0:
        result += "Plang"

    elif number % 7 == 0:
        result += "Plong"

    else:
        result = str(number)

    return result