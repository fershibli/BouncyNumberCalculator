'''
Author: Fernando Luiz Neme Chibli
Date: 2019/04/29

This code will find the least number that has 99% or more of bouncy numbers in its collection.
For performance purpouses, this verification will start at 21780.
'''
from BouncyTools import BouncyList

def main():
    current_range = 24274
    bouncy_list_object=BouncyList()
    while bouncy_list_object.bouncy_percentage<0.99:
        bouncy_list_object.setNewCollection(range(1,current_range))
        bouncy_list_object.run()
        current_range+=1
    print (bouncy_list_object)
    

if __name__ == '__main__':
    main()