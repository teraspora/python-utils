# logtester.py

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

    fallback_type = 'lm'
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


# MAIN CODE:

earth = -1
saturn = 28
neptune = 91
mars = 8

def afunc(n):
    return n + 1488

logvvc('neptune mars', header = 'LOG:  ', type = 'warn')
logvvc('mars earth', header = '* PLANETS * ', type = 'goblin')
logvvc('afunc(11)', type = 'error')