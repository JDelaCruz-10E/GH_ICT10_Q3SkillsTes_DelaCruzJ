from pyscript  import display, document


def sign(e):
    document.getElementById("output").innerHTML = ' '
    name = document.getElementById("name").value
    code = document.getElementById("pass").value

    i = name
    c = code

    uca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'

    if len(i) >= 7:  # username must be at least 7 characters long
        nval = True
    else:
        nval = False

    p2 = False
    p3 = False
    plen = False
    
    if len(p) >= 10:  # password must be at least 10 characters long
        plen = True
        for char in p:
            if char in uca:   # password must contain at least one uppercase letter
                p2 = True
            if char in num:   # password must contain at least one number
                p3 = True

    if p2 == False and plen == True:
        display("*password must contain at least one uppercase letter", target="output")
    if p3 == False and plen == True:
        display("*password must contain at least one number", target="output")
    if plen == False:
        display("*password must be at least 10 characters long", target="output")
        
    pval = p2 and p3 and plen    # validity checking and variable combining for easier checking



    if pval == True:    # validity checking and displaying for password
        display("password is valid", target="output")
    else:
        display("password is invalid, try again!", target="output")
    
    if nval == True:    # validity checking and displaying for username
        display("username is valid", target="output")
    else:
        display("username is invalid, try again!", target="output")

    if pval == True and nval == True:    #if both are correct 
        display("submitted!", target="output")