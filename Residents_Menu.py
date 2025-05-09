import os
import msvcrt as m
import Main_menu
import LGU_MENU
import datetime

Reports_File = "Reports_File.txt"

def clear():
    clear = os.system('cls')

def border():
    for _ in range(120):
        print('-',end='')

def Waste_Report():
    Main_menu.border2()
    print('{:^170}'.format("Waste - Report"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print('{:^170}'.format("─" * 120))
    print("\n")

    Name_Reporter = input('{:>97}'.format("Enter your name                                                  : "))
    Location = input('{:>97}'.format(f"Enter the location of the problem                                : "))
    Issue = input('{:>97}'.format(f"Describe the issue (e.g., Overflow, No Collection)               : "))

    Time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    Status = "In Progress"

    print('{:>117}'.format(f"Date & Time                                                      : {Time}"))
    print('{:>108}'.format(f"Status                                                           : {Status}"))
   
    Report = f"{Time}|{Name_Reporter}|{Location}|{Issue}|{Status}\n"
    
    with open(Reports_File, 'a') as file:    
        file.write(Report)


    print("\n\n")
    print('{:^170}'.format("─" * 120))
    print("\n\n")
    print('{:^170}'.format("Report submitted successfully!"))

def delete_report():
    Main_menu.border2()
    print('{:^170}'.format("Waste Report History"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'':<12}{'No.':<5} {'TIME':<23} {'NAME':<32} {'AREA':<35} {'ISSUE':<45} {'STATUS'}")
    print(f"─" * 178)

    if not os.path.exists(Reports_File):
        print("\n\n\n\n\n")
        print('{:^170}'.format("No reports found."))
        print("\n\n\n\n")
        print("─" * 178)
        m.getch()
        return
    
    with open(Reports_File, 'r') as file:
        reports = file.readlines()

    if not reports:
        print("\n\n\n\n\n")
        print('{:^170}'.format("No reports found."))
        print("\n\n\n\n")
        print("─" * 178)
        m.getch()
        return        

    for i, line in enumerate(reports):
            Time, Name_Reporter, Location, Issue, Status = line.strip().split("|")
            print(f"{'':<12} {i + 1:<5} {Time:<23} {Name_Reporter:<32} {Location:<35} {Issue:<45} {Status:}")
    print("\n\n")

    try:
        report_number = int(input('{:>60}'.format("\nEnter the report number to delete (0 to exit): "))) - 1
        print("\n\n")
        if report_number == -1:
            print('{:^170}'.format("Exiting delete operation..."))

            return
        
        elif 0 <= report_number < len(reports):
            del reports[report_number]
            with open(Reports_File, 'w') as file:
                file.writelines(reports)
            print('{:^170}'.format("Report deleted successfully!"))


        else:
            print('{:^170}'.format("Invalid report number."))

    except ValueError:
        print('{:^170}'.format("Invalid input. Please enter a valid number."))

    print("")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

def View_Report():
    Main_menu.border2()
    print('{:^170}'.format("Waste Report History"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'':<12}{'No.':<5} {'TIME':<23} {'NAME':<32} {'AREA':<35} {'ISSUE':<45} {'STATUS'}")
    print(f"─" * 178)

    if not os.path.exists(Reports_File):
        print("\n\n\n\n\n")
        print('{:^170}'.format("No reports found."))
        print("\n\n\n\n")
        print("─" * 178)
        m.getch()
        return
    
    with open(Reports_File, 'r') as file:
        reports = file.readlines()

    if not reports:
        print("\n\n\n\n\n")
        print('{:^170}'.format("No reports found."))
        print("\n\n\n\n")
        print("─" * 178)
        m.getch()
        return        

    for i, line in enumerate(reports):
            Time, Name_Reporter, Location, Issue, Status = line.strip().split("|")
            print(f"{'':<12} {i + 1:<5} {Time:<23} {Name_Reporter:<32} {Location:<35} {Issue:<45} {Status:}")
            # print("")

    # print(f"─" * 178)
    print("\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

def Waste_Report_Menu():
    while True:
        clear()
        Main_menu.border2()
        print('{:^170}'.format("Waste - Report"))
        print('{:^170}'.format("─" * 50))
        print("\n")

        print('{:>92}'.format("[A] Report an issue"))
        print('{:>89}'.format("[B] View reports"))
        print('{:>92}'.format("[C] Delete a report"))
        print('{:>94}'.format("[D] Back to main menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        selection = input('{:>80}'.format("Enter your choice: ")).upper()
        if selection == 'A':
            clear()
            Waste_Report()
            m.getch()
        elif selection == 'B':
            clear()
            View_Report()
            m.getch()
        elif selection == 'C':
            clear()
            delete_report()
            m.getch()
        elif selection == 'D':
            print("Going back to main menu...")
            m.getch()
            break
        else:
            print("Invalid choice. Please try again.")
            m.getch()

def Menu():
    while True:
        os.system('cls')
        Main_menu.border2()
        print('{:^170}'.format("Waste - Management System"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>89}'.format("[A] Waste Report"))
        print('{:>90}'.format("[B] View Schedule"))
        print('{:>94}'.format("[C] View Announcement"))
        print('{:>100}'.format("[D] View Collection History"))
        print('{:>83}'.format("[E] Logout"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        choice = input('{:>80}'.format("Enter Choice: ")).upper()

        if choice == 'A':
            clear()
            Waste_Report_Menu()
            m.getch()
        elif choice == 'B':
            clear()
            LGU_MENU.View_Schedule()
            m.getch()
        elif choice == 'C':
            clear()
            LGU_MENU.View_Announcement()
            m.getch()
        elif choice == 'D':
            clear()
            LGU_MENU.View_Collection_List()
            m.getch()
        elif choice == 'E':  
            print("Logging out...")
            m.getch()
            Main_menu.main()
        else:
            print("Invalid choice. Please try again.")
            m.getch()