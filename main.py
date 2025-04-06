import subprocess
import sys
from colorama import init, Fore, Style
import hashlib
import os

# Module installation function
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Required modules
required_modules = ['colorama']

# Check if the required modules are installed, if not, install them
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} module not found. Installing...")
        install(module)
    else:
        print(f"{module} module is already installed.")

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.YELLOW + Style.BRIGHT + "    ███╗  ██╗ ███████╗ ██╗  ██╗ ███████╗")
    print(Fore.YELLOW + Style.BRIGHT + "    ████╗ ██║ ██╔════╝ ██║ ██╔╝ ██╔════╝")
    print(Fore.YELLOW + Style.BRIGHT + "    ██╔██╗██║ █████╗   █████╔╝  █████╗  ")
    print(Fore.YELLOW + Style.BRIGHT + "    ██║╚████║ ██╔══╝   ██╔═██╗  ██╔══╝  ")
    print(Fore.YELLOW + Style.BRIGHT + "    ██║ ╚███║ ███████╗ ██║ ╚██╗ ███████╗")
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.GREEN + Style.BRIGHT + "\n          HashKey - Hash Tool")
    print(Fore.CYAN + "="*50 + "\n")

def menu():
    print(Fore.MAGENTA + Style.BRIGHT + "  Select Hash Algorithm:")
    print(Fore.CYAN + " 1. " + Fore.YELLOW + "SHA-256")
    print(Fore.CYAN + " 2. " + Fore.YELLOW + "SHA-1")
    print(Fore.CYAN + " 3. " + Fore.YELLOW + "MD5")
    print(Fore.CYAN + " 4. " + Fore.YELLOW + "SHA-384")
    print(Fore.CYAN + " 5. " + Fore.YELLOW + "SHA-512")
    print(Fore.CYAN + " 6. " + Fore.YELLOW + "BLAKE2b")
    print(Fore.CYAN + " 7. " + Fore.YELLOW + "BLAKE2s")
    print(Fore.CYAN + " 8. " + Fore.GREEN + "Crack Hash with Wordlist")
    print(Fore.CYAN + " 9. " + Fore.RED + "Exit")

def hash_word(word, algorithm):
    algorithms = {
        '1': hashlib.sha256,
        '2': hashlib.sha1,
        '3': hashlib.md5,
        '4': hashlib.sha384,
        '5': hashlib.sha512,
        '6': hashlib.blake2b,
        '7': hashlib.blake2s
    }

    if algorithm in algorithms:
        return algorithms[algorithm](word.encode()).hexdigest()
    else:
        return None

def save_hash_to_file(hash_value):
    with open('hash.txt', 'a') as file:
        file.write(hash_value + '\n')

def crack_hash_with_wordlist(hash_value, algorithm_choice):
    try:
        with open("word.txt", "r") as wordlist:
            for word in wordlist:
                word = word.strip()  # Remove leading/trailing whitespace
                if hash_value == hash_word(word, algorithm_choice):
                    print(Fore.GREEN + f"\nHash cracked! The original word is: {word}")
                    return
            print(Fore.RED + "Hash not found in wordlist.")
    except FileNotFoundError:
        print(Fore.RED + "word.txt file not found.")

def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nSelect An Option (1-9): ")

        if choice == '9':
            print(Fore.RED + Style.BRIGHT + "\nGoodbye! HashKey is Closing...\n")
            break

        if choice == '8':
            hash_value = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nEnter the hash to crack: ")
            crack_hash_with_wordlist(hash_value, input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nSelect the algorithm for cracking: "))
            input(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\nPress Enter to Continue...")
            continue

        word = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nEnter The Word To Hash: ")
        result = hash_word(word, choice)

        if result:
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nHash Result:\n" + Fore.WHITE + result)

            save_option = input(Fore.CYAN + "\nWould You Like To Save The Hash To a File? (Yes/No): ").lower()

            if save_option == 'yes':
                save_hash_to_file(result)
                print(Fore.GREEN + Style.BRIGHT + "\nHash Saved To hash.txt.")
            else:
                print(Fore.YELLOW + Style.BRIGHT + "\nHash Not Saved.")

        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid Selection!")

        input(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\nPress Enter to Continue...")

if __name__ == "__main__":
    main()
