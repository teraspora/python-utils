# logging.py

# Python 3 logging functions
# Author:  John Lynch
# December 2019

# Note: issues re scoping; functions needs to be inline in src file, not imported

def logvv(varstring, header = '***'):
    """
    Print the values of variable names listed in varstring, space-delimited.
    Requires Python 3.8
    """
    names = varstring.split(' ')
    fs = f"f'{header} "
    for name in names:
        fs += "{" + name + "=}, "
    fs = fs[:-2] + ";'"
    print(eval(fs))

def logvvc(varstring, header = '***', type = 'info'):
    """
    Print the values of variable names listed in varstring, space-delimited.
    Requires Python 3.8
    """
    # ANSI Colour codes for terminal output
    CLR_R  = '\u001B[31m'
    CLR_LR = '\u001B[91m'
    CLR_LG = '\u001B[92m'
    CLR_LY = '\u001B[93m'
    CLR_LB = '\u001B[94m'
    CLR_LM = '\u001B[95m'
    CLR_LC = '\u001B[96m'
    RESET  = '\u001B[0m'
    REVERSE_VIDEO = "\u001B[7m"

    fallback_type = 'lb'
    codes = {
        'info':     CLR_LG,
        'warn':     CLR_R,  
        'error':    REVERSE_VIDEO, 
        'lr':       CLR_LR,
        'ly':       CLR_LY,
        'lb':       CLR_LB,
        'lm':       CLR_LM,
        'lc':       CLR_LC
    }
    code = codes[type if type in codes else fallback_type]

    names = varstring.split(' ')
    fs = f"f'{code}{header} "
    for name in names:
        fs += "{" + name + "=}, "
    fs = fs[:-2] + ";{RESET}'"
    print(eval(fs))

# earth = -1
# saturn = 28
# mars = 8
# neptune = 91
# logvv('earth saturn')
# logvvc('neptune mars', header = 'LOG:  ', type = 'warn')
# logvvc('mars earth', header = '* PLANETS * ', type = 'goblin')