#Rainbow text in colorama
#pip install colorama
from colorama import init, Fore, Back
init()

def rainbow():
	rainbowText = ''
	rainbowText += Fore.RED
	rainbowText += 'R'
	rainbowText += Fore.RESET
	rainbowText += Fore.YELLOW #would be orange if orange existed
	rainbowText += 'A'
	rainbowText += Fore.RESET
	rainbowText += Fore.YELLOW
	rainbowText += 'I'
	rainbowText += Fore.RESET
	rainbowText += Fore.GREEN
	rainbowText += 'N'
	rainbowText += Fore.RESET
	rainbowText += Fore.CYAN
	rainbowText += 'B'
	rainbowText += Fore.RESET
	rainbowText += Fore.MAGENTA #indigo
	rainbowText += 'O'
	rainbowText += Fore.RESET
	rainbowText += Fore.BLUE #violet
	rainbowText += 'W'
	rainbowText += Fore.RESET
	return rainbowText
	
print(Back.WHITE+rainbow()) #prints rainbow on white background
	
