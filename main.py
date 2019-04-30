'''
Author: Fernando Luiz Neme Chibli
Date: 2019/04/29

This code will find the least number that has 99% or more of bouncy numbers in its collection.
For performance purpouses, this verification will start at 21780.
'''
from BouncyTools import BouncyList, LeastBouncyFinder
from sys import argv

usage_exemple='\nUsage:\n\tpython %s [integer or float number]'%argv[0]


def byList(current_range,percentage):
    #deprecated
    bouncy_list_object=BouncyList()
    while bouncy_list_object.bouncy_percentage<percentage:
        bouncy_list_object.setNewCollection(range(1, current_range))
        bouncy_list_object.run()
        current_range+=1
    print (bouncy_list_object)

def byFinder(percentage):
    bouncy_finder=LeastBouncyFinder(percentage)
    bouncy_finder.run()
    print(bouncy_finder)

def main():

    if '-h' in argv:
        print(usage_exemple)
        return False

    try:
        percentage=float(argv[1])/100
    except IndexError:
        percentage=0.99
    except ValueError:
        print('You must give a number or 99 will be used as percentage. %s'%(usage_exemple))
        return False
    
    byFinder(percentage)

    input('\n\t(Press return to exit)')
    return True
    

if __name__ == '__main__':
    main()