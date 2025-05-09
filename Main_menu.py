import os
import msvcrt as m
import LGU_MENU
import Residents_Menu


def clear():
    os.system('cls')

def border():
    for _ in range(178):
        print('-',end='')

def border2():
        clear()
        border()
        print("")
        print('{:^170}'.format(" │ │ │┌──│  ┌──┐┌──┐┌──┬──┐┌──  ──┬──┌──┐  │ │ │┌──┐┌── ──┬──┌──  ┌──┬──┐┌──┐┌──┬┌──┐┌── ┌── ┌──┬──┐┌── ┌──┬ ──┬──"))
        print('{:^170}'.format(" │ │ │├──│  │   │  ││  │  │├──    │  │  │  │ │ │├──┤└──┐  │  ├──  │  │  │├──┤│  │├──┤│ ─┐├── │  │  │├── │  │   │  "))
        print('{:^170}'.format(" └─┴─┘└──└─┘└──┘└──┘┴  ┴  ┴└──    ┴  └──┘  └─┴─┘┴  ┴ ──┘  ┴  └──  ┴  ┴  ┴┴  ┴┴  ┴┴  ┴└──┘└── ┴  ┴  ┴└── ┴  ┴   ┴  "))

        print('{:^170}'.format("┌── ┬   ┬ ┌── ──┬──┌── ┌──┬──┐"))
        print('{:^170}'.format("└──┐└─┬─┘ └──┐  │  ├── │  │  │"))
        print('{:^170}'.format(" ──┘  ┴    ──┘  ┴  └── ┴  ┴  ┴"))
        border()
        print("\n\n\n\n\n\n")

def select1():
    while True:
        clear()
        border2()
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:^170}'.format("│[A] Menu|"))
        print("                              ")
        print('{:^170}'.format("│[B] Exit|"))
        print("\n")
        print('{:^170}'.format("─" * 50))
        print("")


        select = input('{:>80}'.format("Select: ")).upper()
        if select == 'A':
            main()
        elif select == 'B':
            print("Exiting...")
            m.getch()
            break
        else:
            print("Invalid Choice...")
            m.getch()

def main():
    while True:
        clear()
        border2()
        print('{:^170}'.format("Waste Management System"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>95}'.format("[A]. Local Government Unit (LGU)"))
        print('{:>77}'.format("[B]. Residents"))
        print('{:>72}'.format("[C]. Exit"))

        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")
        choice = input('{:>80}'.format("Enter your choice: ")).upper()
        if choice == 'A':
            LGU_MENU.Menu()
            m.getch()
        elif choice == 'B':
            Residents_Menu.Menu()
            m.getch()
        elif choice == 'C':
            print("Exiting...")
            m.getch()
            select1()
        else:
            print("Invalid choice. Please try again.")
            m.getch()

if __name__ == "__main__":
    select1()