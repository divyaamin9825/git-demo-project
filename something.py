if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        l.append([input(),float(input())])
    second_highest = sorted(list(set(marks for name, marks in l)))[1]
    print("\n".join([a for a,b in sorted(l) if b == second_highest]))# a is the name of the person with the 2nd highest score and b is the score itself. sorted(l) basically arranges the list acc to the name of the people whose score is given. It is to deal with the part that 2 or more people can score the 2nd highest score and that they should be displayed in alphabetical order
