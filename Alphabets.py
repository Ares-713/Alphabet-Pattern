# Alphabets
def A():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space - 1)) +"$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space - 1))
    string += ("$\n")

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
           string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")
    
    return string

def B():
    string = ""
    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space - 1)) +"$\n")

    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space - 1)) +"$\n")

    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    return string

def C():
    string = ""

    # Horizontal Line
    length_hl = 4
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space - 1))
    string += ("$\n")

    # Vertical Line
    height_vl = 5
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 4
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space - 1))
    string += ("$\n")

    return string

def D():
    string = ""

    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 5
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space + 2)) +"$\n")


    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    return string

def E():
    string = ""
    
    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 2
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 2
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def F():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 2
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 3
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")
    
    return string

def G():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 2
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == (1 or 2):
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += "$\n"

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")


    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def H():
    string = ""

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")
    return string

def I():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")


    # Vertical Line
    height_vl = 5
    initial_space = 2
    for size_vl in range(height_vl):
        string += (("  " * initial_space) + "* " + (" " * (5)) + "$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def J():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")


    # Vertical Line
    height_vl = 5
    initial_space = 2
    for size_vl in range(height_vl):
        string += (("  " * initial_space) + "* " + (" " * (5)) + "$\n")

   # Horizontal Line
    length_hl = 3
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (8 - length_hl - initial_space))
    string += ("$\n")

    return string

def K():
    string = ""

    # Double Bars
    height_db = 1
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (5 - height_db - mid_space)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 2
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 1
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")
    
    # Double Bars
    height_db = 1
    mid_space = 0
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (8 - height_db - mid_space)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 1
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 2
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (5 - height_db - mid_space)) +"$\n")
    
    return string

def L():
    string = ""

    # Vertical Line
    height_vl = 6
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def M():
    string = ""

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl in range(1, 4):
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += "$\n"

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl in range(2, 3):
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += "$\n"

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 3:
            string += ("  ")
        elif size_hl == 2:
            string += ("* *")
        else:
            string += ("*")
    string += (" " * (7 - length_hl - initial_space))
    string += "$\n"

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 3:
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += "$\n"

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")
    
    return string

def N():
    string = ""

    # Double Bars
    height_db = 1
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (5 - height_db - mid_space)) +"$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 2 or size_hl == 3:
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(9):
        if size_hl == 1 or size_hl == 2 or size_hl in range(4,8):
            string += (" ")
        else:
            string += ("*")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 3:
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(9):
        if size_hl == 6 or size_hl == 7 or size_hl in range(1,5):
            string += (" ")
        else:
            string += ("*")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 2:
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (5 - height_db - mid_space)) +"$\n")

    return string

def O():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 5
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (4 - mid_space)) +"$\n")

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    return string

def P():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")

    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Vertical Line
    height_vl = 3
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    return string

def Q():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 2 or size_hl == 3:
            string += ("  ")
        else:
            string += ("* ")
    string += "$\n"

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line
    length_hl = 1
    initial_space = 3
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def R():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 2
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (6 - height_db - mid_space)) +"$\n")

    # Horizontal Line
    length_hl = 4
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    # Double Bars
    height_db = 3
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (7 - height_db - mid_space)) +"$\n")

    return string

def S():
    string = ""

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")


    # Vertical Line
    height_vl = 2
    for size_vl in range(height_vl):
        string += ("* " + (" " * (9)) + "$\n")

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")


    # Vertical Line
    height_vl = 2
    initial_space = 4
    for size_vl in range(height_vl):
        string += (("  " * initial_space) + "* " + (" " * (1)) + "$\n")

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    return string

def T():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")


    # Vertical Line
    height_vl = 6
    initial_space = 2
    for size_vl in range(height_vl):
        string += (("  " * initial_space) + "* " + (" " * (5)) + "$\n")
    return string

def U():
    string = ""

    # Double Bars
    height_db = 6
    mid_space = 3
    for size_db in range(height_db):
        string += ("* " + ("  " * mid_space) + "* " + (" " * (4 - mid_space)) +"$\n")

    # Horizontal Line
    length_hl = 3
    initial_space = 1
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (7 - length_hl - initial_space))
    string += ("$\n")

    return string

def V():
    string = ""

    # Double Bars
    height_db = 1
    mid_space = 11
    initial_space = 0
    string += (("  " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (2)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 9
    initial_space = 1
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (3)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 7
    initial_space = 2
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (4)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 5
    initial_space = 3
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (5)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    initial_space = 4
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (6)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 1
    initial_space = 5
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (7)) +"$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 3:
            string += ("  ")
        else:
            string += ("* ")
    string += (" " * (10 - length_hl - initial_space))
    string += "$\n"

    return string

def W():
    string = ""

    # Double Bars
    height_db = 3
    mid_space = 5
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (10- height_db - mid_space)) +"$\n")

    # Horizontal Line (Broken)
    length_hl = 7
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 2 or size_hl == 4 or size_hl == 5:
            string += (" ")
        else:
            string += ("*")
    string += (" " * (9 - length_hl - initial_space))
    string += "$\n"

    # Horizontal Line (Broken)
    length_hl = 7
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 1 or size_hl == 3 or size_hl == 5:
            string += (" ")
        else:
            string += ("*")
    string += (" " * (9 - length_hl - initial_space))
    string += "$\n"

    # Horizontal Line (Broken)
    length_hl = 7
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl == 2 or size_hl == 3 or size_hl == 4:
            string += (" ")
        else:
            string += ("*")
    string += (" " * (9 - length_hl - initial_space))
    string += "$\n"

    # Double Bars
    height_db = 1
    mid_space = 5
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (8- height_db - mid_space)) +"$\n")

    return string

def X():
    string = ""

    # Double Bars
    height_db = 1
    mid_space = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (2)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    initial_space = 1
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (3)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 1
    initial_space = 2
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (4)) +"$\n")

    # Horizontal Line (Broken)
    length_hl = 5
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 3:
            string += (" ")
        else:
            string += ("*")
    string += (" " * (9 - length_hl - initial_space))
    string += "$\n"

    # Double Bars
    height_db = 1
    mid_space = 1
    initial_space = 2
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (4)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    initial_space = 1
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (3)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 5
    initial_space = 0
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (2)) +"$\n") 

    return string

def Y():
    string = ""

    # Double Bars
    height_db = 1
    mid_space = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (2)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 3
    initial_space = 1
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (3)) +"$\n")

    # Double Bars
    height_db = 1
    mid_space = 1
    initial_space = 2
    string += ((" " * initial_space))
    for size_db in range(height_db):
        string += ("*" + (" " * mid_space) + "*" + (" " * (4)) +"$\n")

    # Vertical Line
    height_vl = 4
    initial_space = 3
    for size_vl in range(height_vl):
        string += ((" " * initial_space) + "*" + (" " * (5)) + "$\n")
    
    return string

def Z():
    string = ""

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    # Horizontal Line (Broken)
    length_hl = 10
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 6:
            string += (" ")
        else:
            string += ("*")
    string += " $\n"

    # Horizontal Line (Broken)
    length_hl = 10
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 5:
            string += (" ")
        else:
            string += ("*")
    string += " $\n"

    # Horizontal Line (Broken)
    length_hl = 10
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 4:
            string += (" ")
        else:
            string += ("*")
    string += " $\n"

    # Horizontal Line (Broken)
    length_hl = 10
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 3:
            string += (" ")
        else:
            string += ("*")
    string += " $\n"

    # Horizontal Line (Broken)
    length_hl = 10
    initial_space = 0
    string += ((" " * initial_space))
    for size_hl in range(length_hl):
        if size_hl != 2:
            string += (" ")
        else:
            string += ("*")
    string += " $\n"

    # Horizontal Line
    length_hl = 5
    initial_space = 0
    string += (("  " * initial_space))
    for size_hl in range(length_hl):
        string += ("* ")
    string += (" " * (6 - length_hl - initial_space))
    string += ("$\n")

    return string

def Space():
    string = ""

    # Double Bars
    height_db = 7
    mid_space = 1
    for size_db in range(height_db):
        string += ("  " + ("  " * mid_space) + "  " + (" " * (4 - height_db - mid_space)) +"$\n")

    return string

name = input("Enter String: ")
name = name.upper()
alpha_string = ""

for index in range(len(name)):
    if name[index] == "A":
        alpha_string += (A())
    elif name[index] == "B":
        alpha_string += (B())
    elif name[index] == "C":
        alpha_string += (C())
    elif name[index] == "D":
        alpha_string += (D())
    elif name[index] == "E":
        alpha_string += (E())
    elif name[index] == "F":
        alpha_string += (F())
    elif name[index] == "G":
        alpha_string += (G())
    elif name[index] == "H":
        alpha_string += (H())
    elif name[index] == "I":
        alpha_string += (I())
    elif name[index] == "J":
        alpha_string += (J())
    elif name[index] == "K":
        alpha_string += (K())
    elif name[index] == "L":
        alpha_string += (L())
    elif name[index] == "M":
        alpha_string += (M())
    elif name[index] == "N":
        alpha_string += (N())
    elif name[index] == "O":
        alpha_string += (O())
    elif name[index] == "P":
        alpha_string += (P())
    elif name[index] == "Q":
        alpha_string += (Q())
    elif name[index] == "R":
        alpha_string += (R())
    elif name[index] == "S":
        alpha_string += (S())
    elif name[index] == "T":
        alpha_string += (T())
    elif name[index] == "U":
        alpha_string += (U())
    elif name[index] == "V":
        alpha_string += (V())
    elif name[index] == "W":
        alpha_string += (W())
    elif name[index] == "X":
        alpha_string += (X())
    elif name[index] == "Y":
        alpha_string += (Y())
    elif name[index] == "Z":
        alpha_string += (Z())
    else:
        alpha_string += (Space())

split = alpha_string.split("$\n")

line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""
line7 = ""

for line in range(len(split)):
    if line % 7 == 0:
        line1 += split[line]
    elif line % 7 == 1:
        line2 += split[line]
    elif line % 7 == 2:
        line3 += split[line]
    elif line % 7 == 3:
        line4 += split[line]
    elif line % 7 == 4:
        line5 += split[line]
    elif line % 7 == 5:
        line6 += split[line]
    else:
        line7 += split[line]

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

# END