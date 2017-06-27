#Colorama test
#pip install colorama
from colorama import init, Fore, Back, Style
init()

#RGB text - all physics colours supported plus BLACK and WHITE. RESET resets the text effect
print(Fore.RED+'Red')
print(Fore.GREEN+'Green')
print(Fore.BLUE+'Blue')
print(Fore.RESET)

#RGB background - same as above but RESET now resets the background effect
print(Back.RED+'Red')
print(Back.GREEN+'Green')
print(Back.BLUE+'Blue')
print(Back.RESET)


