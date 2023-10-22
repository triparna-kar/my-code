import sys, os


print("1: " + str(sys.path[0]))
print("2: " + str(sys.argv[0]))
print("3: " + str(os.path.dirname(sys.argv[0])))
print("4: " + str(os.path.abspath(os.path.dirname(sys.argv[0]))))
print("5: " + str(os.path.dirname(os.path.abspath(sys.argv[0]))))
print("6: " + str(__file__))
print("7: " + str(os.path.dirname(__file__)))