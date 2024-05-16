###########################################################################################
# Name: Norman Cook
# Date: 6/27/2019
# Description: printing all lines to the son 99 bottles of beer on the wall with
# correct grammar
###########################################################################################

# the algorithm implemented recursively
def passSomeBeers(n):
  print "{} bottles of beer on the wall.".format(n)
  print "{} bottles of beer.".format(n)
  print "Take one down, pass it around."
  n = n - 1

  # fixing the grammatical error for when the number of beers is one
  if (n == 1):
    print "{} bottle of beer on the wall.".format(n)
    print
    print "{} bottle of beer on the wall.".format(n)
    print "{} bottle of beer.".format(n)
    print "Take one down, pass it around."
    n = n - 1
    print "{} bottles of beer on the wall.".format(n)
    return

  print "{} bottles of beer on the wall.".format(n)
  print

  # rewrite passSomeBeers function recursively
  passSomeBeers(n)

###############################################
# MAIN PART OF THE PROGRAM
###############################################

# call the function passSomeBeers()
passSomeBeers(99)

