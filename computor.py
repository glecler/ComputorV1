#!/usr/bin/python3

import sys

class Member:
    def __init__(self):
        self.member = ""
        self.factors = []
        self.powers = []

class Equation:
    def __init__(self, input):
        self.members = polyparse(input)

def sqrt(f):
    tmp = 0
    f2 = f / 2

    while(f2 != tmp):
        tmp = f2
        f2 = (f / tmp + tmp) / 2
    return f2

def polyparse(input):

    left = Member()
    right = Member()

    try :
        left.member = input.split(" = ")[0].split()
        left = parse(left.member)
        right.member = input.split(" = ")[1].split()
        right = parse(right.member)
        return (left, right)
    except :
        return (0, 0)

def parse(input):
    sign = ''
    member_info = Member()
    member_info.member = input
    for i in range(0, len(member_info.member), 4):
        member_info.factors.append((str(sign) if sign == '-' else '') + str(member_info.member[i]))
        member_info.powers.append(str(list(member_info.member[i + 2])[2]))
        try :
            sign = member_info.member[i + 3]
        except :
            sign = ''
    return(member_info)

def equalize_degree(left, right):
    length = max(int(max(left.powers)), int(max(right.powers)), 3)
    if (int(max(left.powers)) < int(max(right.powers))):
        swap = right
        right = left
        left = swap
    for i in range(int(max(right.powers)) + 1, length + 1):
        right.powers.append(str(i))
        right.factors.append("0")
    return(left, right)

def reduce_form(left, right):

    reduced_form = left
    reduced_form.member = ""

    (left, right) = equalize_degree(left, right)
    length = int(max(left.powers)) if int(max(left.powers)) > 3 else 3
    for i in range(length + 1):
        try :
            reduced_form.factors[i] = (str(float(left.factors[i]) - float(right.factors[i])))
        except:
            reduced_form.factors.append("0")
            reduced_form.powers.append(str(i))    
    return(reduced_form)

def print_reduced_form_degree(reduced_form):
    degree = -1
    sign = ''

    print("Reduced form : ", end='')
    for i in range(len(reduced_form.powers)):
        if float(reduced_form.factors[i]) != 0:
            degree = i
    if (degree >= 0):
        for i in range(degree + 1):
            if (float(reduced_form.factors[i]) < 0 and i > 0):
                sign = " - "
            elif (float(reduced_form.factors[i]) < 0 and i == 0):
                sign = "-"
            elif (float(reduced_form.factors[i]) >= 0 and i > 0):
                sign = " + "
            print(sign + str(abs(float(reduced_form.factors[i]))) + " * X^" + reduced_form.powers[i], end='')
    else :
        print("0", end='')
        degree = 0
    print(" = 0")
    print("Polynomial degree :", degree)
    return(degree)

def solve_reduced_equation(reduced_form, degree):
    if (degree == 0 and float(reduced_form.factors[0]) != 0):
        print("no solution.")
        return
    if (degree == 2):
        delta = (float(reduced_form.factors[1]) * float(reduced_form.factors[1])) - 4 * float(reduced_form.factors[2]) * float(reduced_form.factors[0])
        if (delta > 0):
            print("Discriminant is stricly positive, the two solutions are:", (-1 * float(reduced_form.factors[1]) - sqrt(delta)) / (2 * float(reduced_form.factors[2])), (-1 * float(reduced_form.factors[1]) + sqrt(delta)) / (2 * float(reduced_form.factors[2])))
        if (delta == 0):
            print("Discriminant equals zero, the unique solution is:", (-1 * float(reduced_form.factors[1])) / (2 * float(reduced_form.factors[2])))
        if (delta < 0):
            print("Discriminant is stricly negative, the two solutions are:", (-1 * float(reduced_form.factors[1])) / (2 * float(reduced_form.factors[2])), " + i * " , sqrt(abs(delta)) / (2 * float(reduced_form.factors[2])), " and ", (-1 * float(reduced_form.factors[1])) / (2 * float(reduced_form.factors[2])), " - i * " , sqrt(abs(delta)) / (2 * float(reduced_form.factors[2])))
        return
    if (degree >= 3):
        print("The polynomial degree is stricly greater than 2, I can't solve")
        return
    print("The solution is:")
    if (degree == 0 and float(reduced_form.factors[0]) == 0):
        print("x E |R.")
    if (degree == 1):
        print("x = ", float(reduced_form.factors[0])/float((-1 * float(reduced_form.factors[1]))))

def check_powers(powers):
    try :
        if (powers[2] == "2"):
            if (powers[1] != "1" or powers[0] != "0"):
                return (0)
    except :
        try :
            if (powers[1] != "1" or (powers[1] == "1" and powers[0] != "0")):
                return (0)
        except :
            if (powers[0] != "0"):
                return (0)
    return (1)

def check_args(arglist):
    if (arglist.members[0] == 0 and arglist.members[1] == 0):
        return 0
    for i in range(2):
        if (check_powers(arglist.members[i].powers) ==  0):
            return 0
    return 1

if (len(sys.argv) == 2):
    input = sys.argv[1]
    arglist = Equation(input)
    if (check_args(arglist) == 0):
        print("Unreadable format. ")
        quit()
    reduced_form = reduce_form(arglist.members[0], arglist.members[1])
    degree = print_reduced_form_degree(reduced_form)
    solve_reduced_equation(reduced_form, degree)