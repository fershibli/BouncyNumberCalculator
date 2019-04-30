"""
Author: Fernando Luiz Neme Chibli
Date: 2019/04/29

This Package have some tools to verify numbers "bouncyness"
"""
def isTreeDigitsBouncy(list):
    #returns if the number made by a list of tree digits is a bouncy number
    #todo: verify list lenght (not necessary in this code)
    return (list[0] > list[1] and list[1] < list[2]) or (list[0] < list[1] and list[1] > list[2])

'''
This class stores all the bouncy occurrences and calculates its percentage, given a number collection
'''
class BouncyList(object):
    bouncy_occurrences = []
    bouncy_percentage = 0
    def __init__(self,number_collection=[]):
        self.number_collection = number_collection
    def __str__(self):
        return 'First Number from Collection: %d\nLast Number from Collection: %d\nLast Bouncy Number from Collection: %s\nAmount of Bouncy Numbers: %d\nProportion of Bouncy Numbers: %s' % (
            self.number_collection[0],
            self.number_collection[-1],
            self.bouncy_occurrences[-1] if len(self.bouncy_occurrences) else 'None',
            len(self.bouncy_occurrences),
            self.getBouncyPercentageStr()
            )
    def getBouncyPercentageStr(self):
        return str(round(self.bouncy_percentage,4)*100)+'%'
    def setNewCollection(self,number_collection):
        self.number_collection = number_collection
        self.bouncy_occurrences = []
        self.bouncy_percentage = 0
    def isBouncy(self,number):
        #returns if the number of any given digits is bouncy
        is_bouncy = False
        previous_digits = []
        for digit in map(int,str(number)):
            previous_digits.append(digit)
            if len(previous_digits) > 2:
                previous_digits=previous_digits[-3:]
                if isTreeDigitsBouncy(previous_digits):
                    is_bouncy = True
                    self.bouncy_occurrences.append(number)
                    break
        return is_bouncy
    def run(self):
        #returns a float from 0 to 1 indicating the percentage of the occurrences of boncy numbers in a list
        self.bouncy_occurrences = []
        self.bouncy_percentage = sum(map(self.isBouncy,self.number_collection))/len(self.number_collection)
        return self.bouncy_percentage
