
# if __name__ == '__main__': 
# This line of code appears after a module (def) to keep the module from running automatically. 
# Anything that is put before this function will be executed before it.

# Module 1

print('This will always be run because it is outside the main method of module #1')

def main():
	print('This is the output of Module #1: {}'.format(__name__))

if __name__ == '__main__': 
	main() 

# when module #1 is imported to other modules, the __name__ of the other modules will become '__main__'
# that is, the module #1 is no longer the main() module in other modules, and thus whatever inside 
# module #1 will not be printed.  