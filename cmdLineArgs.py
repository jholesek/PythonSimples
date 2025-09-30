# 8 lines: this program adds up integers that have been passed as arguments in the command line
import sys
try:
    print (sys.argv)

    total=sum(int(arg) for arg in sys.argv[1:])
    print ('sum = ', total)
except ValueError:
    print ('Please supply integer values only!')

