#!/usr/bin/env python3

#This file is for Around The Clock. For playing check dart.py

#To be done:
#Inputs gegen falsche Eingaben absichern
#Option zum Zwischenchecken der Ergebnisse

from datetime import date

class AroundTheClock:
    def __init__(self):
        self._dict = dict()

    #Add score
    def add(self,value,throws):
        self._dict[value] = throws

    #Correct a score
    def correct(self,value,new_throws):
        self._dict[value] = new_throws

    #Return overall throws
    def throws(self):
        return sum(list(self._dict.values()))
    
    #Defines what the string output for e.g. print is
    def __str__(self):
        return_str = ''
        for key,item in self._dict.items():
            return_str += 'Throws for the score {}: {}\n'.format(key,item)
        return return_str
    
    #Return the Score in format ready for scores.txt
    def tsv_values(self):
        result = '{}\t{}'.format(date.today(),self.throws())
        for entry in list(self._dict.values()):
            result += '\t{}'.format(entry)
        result += '\n'
        return result
    
    #Print the Percentages for each value
    def printPercentage(self):
        result = ''
        for key,item in self._dict.items():
            perc = (item/self.throws())*100
            result += '{:>6}\t{:>6}\t{:>6.2f}%\n'.format(key,item,perc)
        return result

def play_around_the_clock():

    print('This program will ask you for the number of throws for each score.')
    print('If you\'ve sent a wrong number, please input an N in the next prompt.')
    print('To stop the program, type 0 at any point.')
    print('In the end you will have the option, to correct everything.')
    print('Be aware that this program is currently not secure, so only enter what is prompted.')
    
    if input('To start, please enter 1:\n') != '1':
        exit(1)
    
    throw_dict = around_the_clock()    #throws_dict is instance if AroundTheClock
    
    print('Final Stats:')
    overall_throws = throw_dict.throws()
    print('Total throws: {}'.format(overall_throws))
    print('Scores\tThrows\tPerc.')
    
    print(throw_dict.printPercentage())
    
    if input('Should this be written to file? (Y/N)\n') == 'Y':
        result = throw_dict.tsv_values()
        f = open('scores_around_the_clock.txt','a')
        f.write(result)
        f.close()

def around_the_clock():
    throw_dict = AroundTheClock()
    x_prev = None
    
    for x in range(1,22):
        if x == 21:
            x = 25
        throws = int(input('Please insert number of trows for {}:\n'.format(x)))
        if throws == 0:
            if input('Are you sure to cancel? (Y/N)\n') == 'Y':
                exit(0)
            throws = int(input('Please insert number of trows for {}:\n'.format(x)))
        elif throws == 'N' and x_prev:
            prev_throws = int(input('Please insert correction for {}:\n'.format(x_prev)))
            if prev_throws == 0:
                if input('Are you sure to cancel? (Y/N)\n') == 'Y':
                    exit(0)
                prev_throws = int(input('Please insert correction for {}:\n'.format(x_prev)))
            throw_dict.correct(x_prev,prev_throws)
            throws = int(input('Please insert number of throws for {}:\n'.format(x)))
            if throws == 0:
                if input('Are you sure to cancel? (Y/N)\n') == 'Y':
                    exit(0)
                throws = int(input('Please insert number of trows for {}:\n'.format(x)))
        throw_dict.add(x,throws)
        x_prev = x
    return check_around_the_clock_results(throw_dict)

def check_around_the_clock_results(dict):
    while True:
        print(dict)
        correct_or_no = input('Are these correct? (Y/N)\n')
        if correct_or_no == 0:
            if input('Are you sure to cancel? (Y/N)\n') == 'Y':
                exit(0)
            correct_or_no = input('Are these correct? (Y/N)\n')
        elif correct_or_no == 'N':
            x_to_correct = int(input('Please enter the number, you want to correct:\n')) #dunno why the hell, but int is needed here to not get 2 different keys
            if x_to_correct == 0:
                if input('Are these correct? (Y/N)\n') == 'Y':
                    exit(0)
                x_to_correct = int(input('Please enter the number, you want to correct:\n'))
            new_score = int(input('Enter the new score for {}:\n'.format(x_to_correct)))
            if new_score == 0:
                if input('Are you sure to cancel? (Y/N)\n'):
                    exit(0)
                new_score = int(input('Enter the new score for {}:\n'.format(x_to_correct)))
            dict.correct(x_to_correct,new_score)
        elif correct_or_no == 'Y':
            return dict