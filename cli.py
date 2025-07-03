from pyfiglet import figlet_format
from  os import system,name
import sys,time
from main import *
def show_banner():
    system('clear' if name == 'posix' else 'cls')  # clear terminal

    banner = figlet_format("SafePass", font="slant")
    print(colored(banner, "green"))

    subtitle = "🔐 Password Strength & Weakness Checker"
    print(colored(subtitle.center(70), "yellow"))
    type_effect(colored("By Ragul", "cyan"))
    print("-" * 70)
    time.sleep(1)
def type_effect(text, delay=0.05):
    sys.stdout.write("".center(30))
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
def run_cli():
    while True:
        print(colored("\n🔐 Enter your password to analyze (type x for exit):", "yellow"))
        password = input(colored(">>> ", "cyan"))
        if password.lower()=="x":
            exit()
        result = check_password(password)[0]
        print(colored("\n📊 Audit Result:", "magenta"))
        print(colored(result, "white"))

        ask_gen = input(colored("\n🔄 Want me to generate a secure password? (yes/no): ", "green")).lower()
        if ask_gen in ("yes", "y", "ok"):
            suggestion = generate_password()
            print(colored(f"\n🛡️ Suggested Strong Password: {suggestion}", "blue"))
show_banner()
run_cli()
