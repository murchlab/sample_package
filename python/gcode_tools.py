import re
import os


def drill_tool(path, Z, pecking=True):

    Z_pecking = 0.05   # in
    Z_feedrate = 4    # in/min
    Z_init = 0.25     # in
    Z_fastmove = 0.1  # in
    Z_final = 1       # in
    Fast_Move = 50    # in/min
    Delta_N = 5

    file = open(path, "r+")
    # Here the head of a g-code file is defined to be any commands comes before (and including) the tool changing one.
    N = Delta_N
    ishead = True
    XY_list = []
    XY_last = (None, None)
    output = ''

    def gstr(num):
        if num == 0:
            return '0'
        elif num > 0:
            return '{:0.4f}'.format(num).lstrip('0').rstrip('0')
        else:
            return '-' + '{:0.4f}'.format(-num).lstrip('0').rstrip('0')

    for line in file:
        iscomment = line[0] == '\''
        if not ishead:
            if not iscomment:
                X_match = re.search(r'(?:X)(\S*)', line)
                Y_match = re.search(r'(?:Y)(\S*)', line)
                ismatch = False
                if X_match:
                    X = float(X_match[1])
                    ismatch = True
                if Y_match:
                    Y = float(Y_match[1])
                    ismatch = True
                if ismatch:
                    if not (X == XY_last[0] and Y == XY_last[1]):
                        XY_list.append((X, Y))
                        XY_last = (X, Y)
        else:
            if not iscomment:
                N += Delta_N
            output += line
        if not iscomment:
            if re.search(r'T', line):
                ishead = False

    file.close()
    if os.path.isfile(path + ".bak"):
        os.remove(path + ".bak")
    os.rename(path, path + ".bak")

    output += 'N' + str(N) + " G00 G90" + ' X' + gstr(XY_list[0][0]) + ' Y' + gstr(XY_list[0][1]) + '\n'
    N += Delta_N
    output += 'N' + str(N) + " G01 Z" + gstr(Z_init) + " F" + gstr(Fast_Move) + "\n"
    N += Delta_N

    def fast_move(output, N, X, Y):
        output += 'N' + str(N) + " G01" + ' X' + gstr(X) + ' Y' + gstr(Y) + " F" + gstr(Fast_Move) + '\n'
        N += Delta_N
        return output,  N

    def drill(output, N, X, Y, Z):
        output += 'N' + str(N) + " G01 Z" + gstr(Z) + " F" + gstr(Z_feedrate) + "\n"
        N += Delta_N
        output += 'N' + str(N) + " G01 Z" + gstr(Z_fastmove) + " F" + gstr(Z_feedrate) + "\n"
        N += Delta_N
        return output, N

    first_drill = True
    if pecking:
        for X, Y in XY_list:
            Z_n = 0
            next_pecking = True
            if first_drill:
                first_drill = False
            else:
                output, N = fast_move(output, N, X, Y)
            while next_pecking:
                Z_n -= Z_pecking
                if Z_n < Z:
                    Z_n = Z
                    next_pecking = False
                output, N = drill(output, N, X, Y, Z_n)
    else:
        for X, Y in XY_list:
            if first_drill:
                first_drill = False
            else:
                output, N = fast_move(output, N, X, Y)
            output, N = drill(output, N, X, Y, Z)

    output += 'N' + str(N) + " G80 Z" + gstr(Z_final) + "\n"
    N += Delta_N
    output += 'N' + str(N) + " M30\n"
    file = open(path, "w")
    file.write(output)
    file.close()


def mill_tool(path):
    file = open(path, "r+")
    output = ''

    for line in file:
        line = line.replace(' G40', '')
        line = line.replace(' G41', '')
        output += line

    file.close()
    if os.path.isfile(path + ".bak"):
        os.remove(path + ".bak")
    os.rename(path, path + ".bak")

    file = open(path, "w")
    file.write(output)
    file.close()