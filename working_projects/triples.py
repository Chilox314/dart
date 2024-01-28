#!/usr/bin/env python3

from datetime import date

def play_triples(t):
    print_instructions()
    score = TripleDarts(t)
    while True:
        i = input('Please enter your Score: (0,1,2,3)\n')
        if i == '00':
            if input('Do you really want to end? (Y/N)\n') == 'Y':
                break
        elif i == 'e':
            e = input('Which one do you want to decrement? (0,1,2,3)\n')
            score.edit(e)
        elif i in ['0','1','2','3']:
            score.add(i)
        else:
            print('"{}" is not allowed as an input. Please try again. (0,1,2,3,00,e)'.format(i))
    print(score)
    if input('Should the score be written to file? (Y/N)\n') == 'Y':
        result = score.tsv_values()
        f = open('scores_triples.txt','a')
        f.write(result)
        f.close()
    else:
        exit(0)

class TripleDarts:
    def __init__(self,triple):
        self._score_dict = dict()
        self._score_dict['throws'] = 0
        self._score_dict['0'] = 0
        self._score_dict['1'] = 0
        self._score_dict['2'] = 0
        self._score_dict['3'] = 0
        self._triple = triple
    
    def add(self,score):
        self._score_dict[score] += 1
        self._score_dict['throws'] += 1
    
    def edit(self,score):
        self._score_dict[score] -= 1
        self._score_dict['throws'] -= 1

    def __str__(self):
        zero = self._score_dict['0']
        one = self._score_dict['1']
        two = self._score_dict['2']
        three = self._score_dict['3']
        throws = self._score_dict['throws']

        s = 'Your scores:\n'
        s += 'Triple {}:            {}\t({:.2f}%)\n'.format(self._triple,three,100*three/throws)
        s += 'Single and Double {}: {}\t({:.2f}%)\n'.format(self._triple,two,100*two/throws)
        s += 'Left and right field: {}\t({:.2f}%)\n'.format(one,100*one/throws)
        s += 'No Score:             {}\t({:.2f}%)\n'.format(zero,100*zero/throws)
        s += 'Overall Throws:       {}'.format(throws)

        return s
    
    def tsv_values(self):
        zero = self._score_dict['0']
        one = self._score_dict['1']
        two = self._score_dict['2']
        three = self._score_dict['3']
        throws = self._score_dict['throws']

        result = '{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(date.today(),self._triple,throws,three,two,one,zero)
        return result

def print_instructions():
    print('Instructions:')
    print('You will get asked for your score for each thrown dart.')
    print('The programm differentiates between the targeted triple (3), \
          the single or double (2), the fields next to the targeted field (1) \
          or any other score (0). When asked, please enter the corresponding numbers \
          to the commandline.')
    print('To end, enter an "00". You will then be asked, if the score should be written to file.')
    print('To edit the last input, enter "e".')