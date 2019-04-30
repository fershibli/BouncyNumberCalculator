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
This class searches for the least bouncy number given a percentage of occurence from 1.
This class DOES NOT stores all the bouncy occurrences.
New approach to attempt a better performance.
'''
class LeastBouncyFinder(object):
    bouncy_amount = 0
    bouncy_percentage = 0
    last_number = 0
    def __init__(self, percentage_to_find_least_bouncy):
        self.percentage_to_find_least_bouncy = percentage_to_find_least_bouncy
    def __str__(self):
        return '\n\t----- Result for %.3f%% ------\n\nLast Bouncy Number:\t\t %s\nAmount of Bouncy Numbers:\t %d\nProportion of Bouncy Numbers:\t %s' % (
            self.percentage_to_find_least_bouncy*100,
            self.last_number,
            self.bouncy_amount,
            self.bouncy_percentage
            )
    def getBouncyPercentageStr(self):
        return str(round(self.bouncy_percentage, 5)*100)+'%'
    def isBouncy(self, number):
        #returns if the number of any given digits is bouncy
        is_bouncy = False
        previous_digits = []
        for digit in map(int, str(number)):
            previous_digits.append(digit)
            if len(previous_digits) > 2:
                previous_digits=previous_digits[-3:]
                if isTreeDigitsBouncy(previous_digits):
                    is_bouncy = True
                    break
        return is_bouncy
    def run(self):
        print('Calculating for {:2.2%} ...'.format(self.percentage_to_find_least_bouncy))
        while(self.bouncy_percentage<self.percentage_to_find_least_bouncy):
            self.last_number+=1
            if self.isBouncy(self.last_number):
                self.bouncy_amount+=1
                self.bouncy_percentage = self.bouncy_amount/self.last_number
                print("\tPercentage: {:2.6%}\tNumber: {}".format(self.bouncy_percentage,self.last_number), end="\r")
        print('\nDone!')



'''
(deprecated)
This class stores all the bouncy occurrences and calculates its percentage, given a number collection
'''
class BouncyList(object):
    bouncy_occurrences = []
    bouncy_percentage = 0
    def __init__(self, number_collection=[]):
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
        return str(round(self.bouncy_percentage, 4)*100)+'%'
    def setNewCollection(self, number_collection):
        self.number_collection = number_collection
        self.bouncy_occurrences = []
        self.bouncy_percentage = 0
    def isBouncy(self, number):
        #returns if the number of any given digits is bouncy
        is_bouncy = False
        previous_digits = []
        for digit in map(int, str(number)):
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
        self.bouncy_percentage = sum(map(self.isBouncy, self.number_collection))/len(self.number_collection)
        return self.bouncy_percentage
