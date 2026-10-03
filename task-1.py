# Functions
# define a function:--> def function_name_here():
# inside the functions paranthasis like this:-->
#               def my_function(name, age, work):
#       name, age, work are called parameters

def main():
    name = str(input("Enter the hacker's name: "))
    hacker_printer(name)

def hacker_printer(name):
    name = name.upper()
    print(f"\033[91mThis packet is from {name}-HACKER\033[0m")
    print(f"\033[91mThis packet is from {name}-HACKER'S AUTHENTICATION\033[0m")

if __name__ == '__main__':
    main()