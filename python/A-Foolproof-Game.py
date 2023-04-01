#############################################################################
# Name: Norman Cook
# Date: 8/13/2019
# Description: Implementation of a Heads and tails game where group A gets
#   a point for both coins being heads, group B gets a point for both coins 
#   being tails, and the professor gets a point if either coin lands on 
#   heads and the other is tails.
#############################################################################
from random import *

# method for the heads and tails game
def headsandtails(games, tosses):
  WinA = WinB = Winprof = 0
  WinperctA = WinperctB = Winperctprof = 0
  gamecnt = 0

  # iterative loop for each game that needs to be played
  while gamecnt < games:
    A = B = prof = 0
    TossperctA = TossperctB = Tossperctprof = 0
    tosscnt = 0

    print "Game {}:".format(gamecnt)

    # iterative loop for each toss in a single game
    while tosscnt < tosses:

      # establish two flipped coins
      flip1 = randrange(2)
      flip2 = randrange(2)

      # determine which group is the winner of the coin toss
      if (flip1 == 0 and flip2 == 0):
        A += 1
      elif (flip1 == 1 and flip2 == 1):
        B += 1
      else:
        prof += 1

      tosscnt += 1

    # calculate the percentages for each group after one game
    TossperctA = percent(A, tosses)
    TossperctB = percent(B, tosses)
    Tossperctprof = percent(prof, tosses)
    
    print "  Group A: {} ({:.2f}%); Group B = {} ({:.2f}%); Prof = {} ({:.2f}%)".format(A, TossperctA, B, TossperctB, prof, Tossperctprof)

    # determine the winner of a single game
    if (A > B and A > prof):
      WinA += 1
    elif (B > A and B > prof):
      WinB += 1
    elif (prof > A and prof > B):
      Winprof += 1

    gamecnt += 1

  # calculate the percentages of wins for each group  
  WinperctA = percent(WinA, games)
  WinperctB = percent(WinB, games)
  Winperctprof = percent(Winprof, games)

  print "Wins: Group A = {} ({:.2f}%); Group B = {} ({:.2f}%); Prof = {} ({:.2f}%)".format(WinA, WinperctA, WinB, WinperctB, Winprof, Winperctprof)

# method for calculating percentage  
def percent(num, den):
  return (num / float(den)) * 100

######################################################
# main
######################################################

# ask the user how many games to play
# ask the user how many tosses are in each game
games = input("How many games? ")
tosses = input("How many coin tosses per game? ")

# call the heads and tails game
headsandtails(games, tosses)
