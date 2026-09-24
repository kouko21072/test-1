
import statistics



def extremy(seznam):
    return (min(seznam), max(seznam))

def prumer(seznam):
    return sum(seznam) / len(seznam)

def median(seznam):
    length = len(seznam)
    if (length % 2 == 0):
        return (seznam[length // 2] + seznam[(length // 2) - 1]) / 2
    else: 
        return seznam[length // 2]
def ukol1():
    seznam = []

    while 1:
        try:
            num = int(input())
            if num <= 0:
                break;
            seznam.append(num)
        except ValueError:
            print("Neni cislo")
            break


    if (len(seznam) == 0):
        print("Prazdny seznam")
        return


    seznam.sort()
    print("Serazeno:", seznam)
    print("Prumer: ", prumer(seznam))
    
    print("Extremy: ", extremy(seznam))
    print("Median:", median(seznam))

ukol1()


def ukol2():
    castky =  [1000, 1050, 1080, 1020, 1120, 1160, 1100, 1150, 1230, 1200, 1260, 1230]

