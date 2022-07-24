import sys
print ("Hexadecimal is the highest this adder can count.\nProgram uses integers only")
'''Here is are list of all the possible number systems as I wanted to make them myself.
I have decided I will make a funtion that converts but will not call it.
It will be able to convert to any number system within the restriction of this code.'''
systems_dict = {
    "hexa"    :  [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'],
    "penta"   :  [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e'],
    "tetra"   :  [0,1,2,3,4,5,6,7,8,9,'a','b','c','d'],
    "trid"    :  [0,1,2,3,4,5,6,7,8,9,'a','b','c'],
    "duo"     :  [0,1,2,3,4,5,6,7,8,9,'a','b'],
    "unde"    :  [0,1,2,3,4,5,6,7,8,9,'a'],
    "denary"  :  [0,1,2,3,4,5,6,7,8,9],
    "nonary"  :  [0,1,2,3,4,5,6,7,8],
    "octal"   :  [0,1,2,3,4,5,6,7],
    "septe"   :  [0,1,2,3,4,5,6],
    "senary"  :  [0,1,2,3,4,5],
    "quin"    :  [0,1,2,3,4],
    "quater"  :  [0,1,2,3],
    "tern"    :  [0,1,2],
    "bina"    :  [0,1]
    }

def are_numbers(item):
    answer = True
    if type(item) is list:
        for i in item:
            if i.isdigit():

                continue
            else :
                answer = False
                break

    else :
        print ("This function was expecting a list of numbers")
        answer = False

    return answer

def rough_convert(num,base):
    if base > 16 and base < 2:
        print("Numerical System not covered by this program yet.")
        return
    bases = [0,"bina",
            "tern","quater",
            "quin","senary",
            "septe","octal",
            "nonary","denary",
            "unde","duo","trid",
            "tetra","penta","hexa"]
    wrd_base = bases[base-1]
    num_sys_lst = systems_dict[wrd_base]
    fin = ""
    cnt = 0
    while cnt != num :
        here = num % base
        fin = str(num_sys_lst[here]) + fin
        num = num//base
    print("0"+fin)

def smooth_convert(num, base):
    if base > 16 and base < 2:
        print("Numerical System not covered by this program yet.")
        return
    if base < 10 :
        fin = ""
        cnt = 0
        while cnt != num :
            here = num % base
            fin = str(here) + fin
            num = num//base
        print("0"+fin)
    elif base == 10 :
        print(num)
    elif(base > 10):
        extras = ['a','b','c','d','e','f','g','h','i','j']
        fin = ""
        cnt = 0
        while cnt != num :
            here = num % base
            if here > 9:
                here -= 9
                fin = str(extras[here-1]) + fin
            else:
                fin = str(here) + fin
            num = num//base
        print("0"+fin)

def calc(item):
    if not are_numbers(item):
        print ("Was expecting numbers only")
        return
    num1 = int(item[0])
    num2 = int(item[1])
    count_system = int(item[2])
    final = num1 + num2
    rough_convert(final, count_system)
    smooth_convert(final, count_system)



def main():

    numlist = []
    if len(sys.argv) == 1 :
        print("Input will be take from here but next time call the program with input")

        numlist = (input("Please input two numbers you wanna add and the number system you wanna use. \ne.g. 22 16 16 means you want 22+16 in hexadecimal\n")).split(" ")
        if len(numlist) == 3:
            calc(numlist)
        else:
            print("Please input two numbers you wanna add and the number system you wanna use next time!!")

    elif len(sys.argv) != 4 :
        print("Please input two numbers you wanna add and the number system you wanna use next time!!")
        return

    elif len(sys.argv) == 4:
        numlist = sys.argv[1::]
        calc(numlist)
    else:
        print("I don't know how you got here but welldone")


main()
