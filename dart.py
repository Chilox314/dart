#!/usr/bin/env python3

#IMPORT FEHLER IST NICHT REAL!!! ARGUMENTE BEIM START NÖTIG!!!

#Möglichkeit einer Session mit Sessionstats und -vergleich (Alias 3x hintereinander spielen und dann den Direktvergleich haben)
#Option zum plotten adden
#GUI bauen (TKinter?)

from atc import play_around_the_clock
from triples import play_triples
import sys, argparse

def main():
    args = paste_command_line(sys.argv[1:])
    if args.plot:
        print('plot')
        plot_scores_txt()
    elif args.aroundTheClock:
        play_around_the_clock()
    elif args.triples:
        play_triples(input('What triple do you like to focus on?\n'))
    else:
        print('Please use Arguments. See ./dart.py -h')

#here is the code for plotting
def plot_scores_txt():
    return True

def paste_command_line(argv):
    p = argparse.ArgumentParser(description='This is for playing "Around the clock" or other dart game modes. Have Fun!')

    p.add_argument('--plot','-p',action='store_true')
    p.add_argument('--aroundTheClock','-a',action='store_true',help='Play a game of around the clock')
    p.add_argument('--triples','-t',action='store_true',help='Play a game of throwing triples')

    return p.parse_args(argv)

main()