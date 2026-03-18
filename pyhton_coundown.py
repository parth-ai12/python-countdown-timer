import time
from colorama import Fore, Style

print(Fore.GREEN + "⏳ Countdown Timer")
print(Style.RESET_ALL)

seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60

    print(Fore.CYAN + f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds -= 1

print(Fore.RED + "\n⏰ Time's up!")
print(Style.RESET_ALL)