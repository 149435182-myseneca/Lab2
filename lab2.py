import sys

def print_args():
    script_name = sys.argv[0]
    print("Script name:", script_name)

    if len(sys.argv) > 1:
        variables = " ".join(sys.argv[1:])
        print("Script and variables:", script_name, variables)

print_args()

def helloWorld():
	print('Hello World')


helloWorld()
