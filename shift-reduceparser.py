def main():
    coordinat = ["0x", "0+", "0*", "0(", "0)", "0$", "0E", "0T", "0F", "1x", "1+", "0*", "1(", "1)", "1$", "1E", "1T", "1F", "2x", "2+", "2*", "2(", "2)", "2$", "2E", "2T", "2F", "3x", "3+", "3*", "3(", "3)", "3$", "3E", "3T", "3F", "4x", "4+", "4*", "4(", "4)", "4$", "4E", "4T", "4F", "5x", "5+", "5*", "5(", "5)", "5$", "5E", "5T", "5F", "6x",
                 "6+", "6*", "6(", "6)", "6$", "6E", "6T", "6F", "7x", "7+", "7*", "7(", "7)", "7$", "7E", "7T", "7F", "8x", "8+", "8*", "8(", "8)", "8$", "8E", "8T", "8F", "9x", "9+", "9*", "9(", "9)", "9$", "9E", "9T", "9F", "ax", "a+", "a*", "a(", "a)", "a$", "aE", "aT", "aF", "yx", "y+", "y*", "y(", "y)", "y$", "yE", "yT", "yF"]
# a->10
# x->id
# y->11
    value = ['S5', "0", "0", "S4", "0", "0", "1", "2", "3", "0", "S6", "0", "0", "0", "Accept", "0", "0", "0", "0", "R2", "S7", "0", "R2", "R2", "0", "0", "0", "0", "R4", "R4", "0", "R4", "R4", "0", "0", "0", "S5", "0", "0", "S4", "0", "0", "8", "2", "3", "0", "R6", "R6", "0", "R6", "R6", "0", "0",
             "0", "S5", "0", "0", "S4", "0", "0", "0", "9", "3", "S5", "0", "0", "S4", "0", "0", "0", "0", "a", "0", "S6", "0", "0", "Sy", "0", "0", "0", "0", "0", "R1", "S7", "0", "R1", "R1", "0", "0", "0", "0", "R3", "R3", "0", "R3", "R3", "0", "0", "0", "0", "R5", "R5", "0", "R5", "R5", "0", "0", "0"]

    input1 = input("Please enter the token: ")
    mystack = ["0"]
    input1 = list(input1)
    newList = finder(input1)
    newList.append("$")
    newList.append("$")

    # print(newList)
    action = " "
    a = stack(action, mystack, newList, coordinat, value)


"""
Rules ---
E->E+T
E->T
T->T*F
T->F
F->(E)
F->id
"""


def finder(input1):
    while ("i" in input1):
        index1 = input1.index("i")
        if ("d" in input1):
            index2 = input1.index("d")
            del input1[index2]
        input1[index1] = "x"
    return input1


def indexer(value, str1):
    list1 = []
    for i in range(len(value)):
        i -= 1

        if (value[i] == str1):
            list1.append(i)
    return max(list1)


def stack(action, mystack, newlist, coordinat, value):
    while (action != 'Accept'):
        if (action == '0'):
            print("INVALID string entered. SYNTAX ERROR!")
            break
        if (action.startswith('R')):
            print("if", mystack)
            index1 = coordinat.index(mystack[-2]+mystack[-1])
            action = value[index1]
            mystack += action[-1]
            continue
        else:
            # print(mystack)
            mystack += newlist[0]
            # print("myList:",newlist)
            print("My", mystack)
            #del newlist[0]
            index1 = coordinat.index(mystack[-2]+mystack[-1])
            action = value[index1]
            print(action, "----------------------------------------")
            mystack = justAction(action, mystack, newlist)
            continue


def justAction(action, mystack, input):
    if (action.startswith('S')):
        mystack += action[1]
        del input[0]
        return mystack
    if (action == 'R1'):
        # E->E+T
        if ("E" and "T" in mystack):
            print("aaa", mystack)
            index = indexer(mystack, "E")
            del mystack[index+1:]
            print(mystack)
            mystack[index] = "E"
        # print("R1")
        return mystack
    if (action == 'R2'):
        # E->T
        # print("R2")
        if ("T" in mystack):
            index = indexer(mystack, "T")
            print(index)
            del mystack[index+1:]
            mystack[index] = "E"
            #del input[0]
        return mystack
    if (action == 'R3'):
        # T->T*F
        if ("T" and "*" and "F" in mystack):
            index = indexer(mystack, "T")
            index3 = indexer(mystack, "F")
            del mystack[index+1:]
            mystack[index] = "T"
        #del input[0]
        print("R3")
        return mystack
    if (action == 'R4'):
        # T->F
        # print("R4")
        print("aaa", mystack)
        while ("F" in mystack):
            index = indexer(mystack, "F")
            del mystack[index+1:]
            mystack[index] = "T"
        #del input[0]
        return mystack
    if (action == 'R5'):
        # print("R5")
        print(mystack)
        if ("(" and "E" and ")" in mystack):
            index = indexer(mystack, "(")
            index3 = indexer(mystack, ")")
            del mystack[index+1:index3+1]
            mystack[index] = "F"
        #del input[0]
        print(mystack)
        return mystack
    if (action == 'R6'):
        print(mystack)
        # F->id
        if ("x" in mystack):
            index = indexer(mystack, "x")
            del mystack[index+1:]
            mystack[index] = "F"
        # print("R6")
        #del input[0]
        print(mystack)
        return mystack
        # stack(mystack,newlist,value,coordinat)
    if (action == "Accept"):
        print("VALID string entered. ACCEPTED!")


main()
