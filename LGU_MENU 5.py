import os
import msvcrt as m
import Main_menu
import datetime

Reports_File = "Reports_File.txt"

schedules = {"Sunday": "6:00am - 9:00am",
            "Monday": "6:00am - 9:00am", 
            "Tuesday": "6:00am - 9:00am", 
            "Wednesday": "6:00am - 9:00am", 
            "Thursday": "6:00am - 9:00am",
            "Friday": "6:00am - 9:00am", 
            "Saturday": "6:00am - 9:00am"}

def clear():
    os.system('cls')

def border():
    for _ in range(50):
        print('-',end='')

def border1():
    for _ in range(178):
        print('-',end='')

def border2():
        clear()
        border1()
        print("")
        print('{:^170}'.format(" │ │ │┌──│  ┌──┐┌──┐┌──┬──┐┌──  ──┬──┌──┐  │ │ │┌──┐┌── ──┬──┌──  ┌──┬──┐┌──┐┌──┬┌──┐┌── ┌── ┌──┬──┐┌── ┌──┬ ──┬──"))
        print('{:^170}'.format(" │ │ │├──│  │   │  ││  │  │├──    │  │  │  │ │ │├──┤└──┐  │  ├──  │  │  │├──┤│  │├──┤│ ─┐├── │  │  │├── │  │   │  "))
        print('{:^170}'.format(" └─┴─┘└──└─┘└──┘└──┘┴  ┴  ┴└──    ┴  └──┘  └─┴─┘┴  ┴ ──┘  ┴  └──  ┴  ┴  ┴┴  ┴┴  ┴┴  ┴└──┘└── ┴  ┴  ┴└── ┴  ┴   ┴  "))

        print('{:^170}'.format("┌── ┬   ┬ ┌── ──┬──┌── ┌──┬──┐"))
        print('{:^170}'.format("└──┐└─┬─┘ └──┐  │  ├── │  │  │"))
        print('{:^170}'.format(" ──┘  ┴    ──┘  ┴  └── ┴  ┴  ┴"))
        border1()

def Collect_Waste():
    Main_menu.border2()
    print('{:^60}'.format("Collecting waste:"))
    print("\n\n")
    print('{:^165}'.format("─" * 100))
    print("\n")
    Name = input('{:>105}'.format ("Enter Name of the Resident                                            : "))
    Area = input ('{:>105}'.format("Enter Area                                                            : "))
    Waste_Type = input('{:>105}'.format("Enter Type of Waste (e.g., [P] Plastic, [O] Organic, [M] Metal)       : ")).upper()

    if Waste_Type == "P":
        Waste_Type = "Plastic"
    elif Waste_Type == "O":
        Waste_Type = "Organic"
    elif Waste_Type == "M":
        Waste_Type = "Metal"
    else:
            print("\n\n")
            print('{:^165}'.format("─" * 100))
            print("\n\n")
            print('{:^130}'.format("Invalid waste type. Please enter [P], [O], or [M]."))
            m.getch()
            return  

    try:
        Waste_Weight = float(input('{:>105}'.format("Enter Weight of Waste (in kg)                                         : ")))
        print("\n\n")
        print('{:^165}'.format("─" * 100))
    except ValueError:
        print("\n\n")
        print('{:^130}'.format("Invalid weight. Please enter a numeric value."))
        return
    Time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    with open("Waste_Collection_File.txt", 'a') as file:
        file.write(f"{Time}|{Name}|{Area}|{Waste_Type}|{Waste_Weight}\n")

    print("\n\n\n\n")
    print('{:^130}'.format("Waste collection recorded successfully!"))
    print('{:^130}'.format("Press enter key to return to the menu..."))
    m.getch()

def View_Collection_List():
    border2()
    print("\n")
    print('{:^170}'.format("[LGU] Waste Collection List"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐")     
    print(f"{'':<20}{'No.':<5} {'TIME':<25} {'NAME':<40} {'AREA':<40} {'TYPE':<15} {'WEIGHT (kg)':<10}")
    print(f"{'├':>15}{"─" * 147}┤") 


    if not os.path.exists("Waste_Collection_File.txt"):
        print("\n\n\n\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤") 

        m.getch()
        return

    with open("Waste_Collection_File.txt", 'r') as file:
        collections = file.readlines()

    if not collections:
        print("\n\n\n\n\n")
        print("\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    total_weight = 0
    waste_summary = {}


    for i, line in enumerate(collections):
        Time, Name, Area, Waste_Type, Waste_Weights = line.strip().split("|")
        Waste_Weight = float(Waste_Weights)
        total_weight += Waste_Weight

        if Waste_Type in waste_summary:
            waste_summary[Waste_Type] += Waste_Weight
        else:
            waste_summary[Waste_Type] = Waste_Weight

        print(f"{'':<20}{i + 1:<5} {Time:<25} {Name:<40} {Area:<40} {Waste_Type:<15} {Waste_Weight:<10.2f}")
        print(f"{'├':>15}{"─" * 147}┤")
    
    print("\n\n")
    print('{:^50}'.format("Summary:"))
    print('{:>62}'.format(f"Total Waste Collected: {total_weight:.2f} kg"))
    print("")
    print('{:^70}'.format("Waste Types Breakdown:"))
    for waste_type, weight in waste_summary.items():
        print(f" {"":<30} - {waste_type:<15}: {weight:.2f} kg")

    print("\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

def delete_collection():
    border2()
    print("\n")
    print('{:^170}'.format("[LGU] Delete Waste Collection List"))
    print('{:^170}'.format("─" * 53))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐")     
    print(f"{'':<20}{'No.':<5} {'TIME':<25} {'NAME':<40} {'AREA':<40} {'TYPE':<15} {'WEIGHT (kg)':<10}")
    print(f"{'├':>15}{"─" * 147}┤") 


    if not os.path.exists("Waste_Collection_File.txt"):
        print("\n\n\n\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤") 

        m.getch()
        return

    with open("Waste_Collection_File.txt", 'r') as file:
        collections = file.readlines()

    if not collections:
        print("\n\n\n\n\n")
        print("\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    for i, line in enumerate(collections):
        Time, Name, Area, Waste_Type, Waste_Weights = line.strip().split("|")
        Waste_Weight = float(Waste_Weights)

        print(f"{'':<20}{i + 1:<5} {Time:<25} {Name:<40} {Area:<40} {Waste_Type:<15} {Waste_Weight:<10.2f}")
        print(f"{'├':>15}{"─" * 147}┤")
    print("\n\n\n\n")

    try:
        collection_number = int(input('{:>60}'.format("Enter the collection number to delete (0 to exit): "))) - 1
        if collection_number == -1:
            print('{:^170}'.format("Exiting delete operation..."))
            return

        elif 0 <= collection_number < len(collections):
            del collections[collection_number]
            with open("Waste_Collection_File.txt", 'w') as file:
                file.writelines(collections)
            print("\n")
            print('{:^170}'.format("Collection deleted successfully!"))

        else:
            print("\n")
            print('{:^170}'.format("Invalid collection number."))

    except ValueError:
        print("\n")
        print('{:^170}'.format("Invalid input. Please enter a valid number."))


    print("\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))

def Waste_Collection():
    while True:
        clear()
        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste Collection"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>88}'.format("[A] Collect Waste"))
        print('{:>95}'.format("[B] View Collection List"))
        print('{:>92}'.format("[C] Delete Collection"))
        print('{:>92}'.format("[D] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        selection = input('{:>90}'.format("Enter your choice: ")).upper()
        if selection == 'A':
            clear()
            Collect_Waste()
            m.getch()
        elif selection == 'B':
            clear()
            View_Collection_List()
            m.getch()
        elif selection == 'C':
            clear()
            delete_collection()
            m.getch()
        elif selection == 'D':
            print("\nGoing back to main menu...")
            m.getch()
            break
        else:
            print("\nInvalid choice. Please try again.")

def Post_Announcement():
    border2()
    print("\n")
    print('{:^170}'.format("Post Announcement:"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")
    
    print('{:^165}'.format("─" * 120))
    print("\n")
    announcement = input('{:>46}'.format("Enter the announcement: "))
    Time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    with open("Announcement_File.txt", 'a') as file:
        file.write(f"{Time}|{announcement}\n")

    print("\n\n")
    print('{:^165}'.format("─" * 120))
    print("\n\n")
    print('{:>60}'.format("Announcement posted successfully!"))
    print("\n")
    print('{:>67}'.format("Press enter key to return to the menu..."))
    m.getch()

def View_Announcement():
    border2()
    print("\n\n")
    print('{:^170}'.format("[LGU] Announcements"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐") 
    print(f"{'':<15} {'No.':<5} {'TIME':<25} {'ANNOUNCEMENT':<100}")
    print(f"{'├':>15}{"─" * 147}┤")

    if not os.path.exists("Announcement_File.txt"):
        print("\n\n\n\n")
        print('{:^170}'.format("No announcements found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    with open("Announcement_File.txt", 'r') as file:
        announcements = file.readlines()

    if not announcements:
        print("\n\n\n\n")
        print('{:^170}'.format("No announcements found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    for i, line in enumerate(announcements):
        Time, announcement = line.strip().split("|")
        print("")
        print(f"{'':>15} {i + 1:<5} {Time:<25}  {announcement:<100}")
        print("")
        print(f"{'├':>15}{"─" * 147}┤")
        
    print("\n\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

def delete_announcement():
    border2()
    print("\n\n")
    print('{:^170}'.format("[LGU] Delete Announcements"))
    print('{:^170}'.format("─" * 59))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐") 
    print(f"{'':<15} {'No.':<5} {'TIME':<25} {'ANNOUNCEMENT':<100}")
    print(f"{'├':>15}{"─" * 147}┤")

    if not os.path.exists("Announcement_File.txt"):
        print("\n\n\n\n")
        print('{:^170}'.format("No announcements found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    with open("Announcement_File.txt", 'r') as file:
        announcements = file.readlines()


    if not announcements:
        print("\n\n\n\n")
        print('{:^170}'.format("No announcements found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return        

    for i, line in enumerate(announcements):
        Time, announcement = line.strip().split("|")
        print("")
        print(f"{'':>15} {i + 1:<5} {Time:<25}  {announcement:<100}")
        print(f"{'├':>15}{"─" * 147}┤")

    try:
        print("\n")
        announcement_number = int(input('{:>60}'.format("\nEnter the announcement number to delete (0 to exit): "))) - 1
        if announcement_number == -1:
            print('{:^170}'.format("Exiting delete operation..."))
            return

        elif 0 <= announcement_number < len(announcements):
            del announcements[announcement_number]
            with open("Announcement_File.txt", 'w') as file:
                file.writelines(announcements)
            print("\n")
            print('{:^170}'.format("Announcement deleted successfully!"))

        else:
            print("\n")
            print('{:^170}'.format("Invalid announcement number."))

    except ValueError:
        print("\n")
        print('{:^170}'.format("Invalid input. Please enter a valid number."))

    print('{:^170}'.format("Press enter key to return to the menu..."))

def Announcement():
    while True:
        Main_menu.border2()
        print('{:^170}'.format("Announcement Post:"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>92}'.format("[A] Post Announcement"))
        print('{:>98}'.format("[B] View Announcement Posts"))
        print('{:>99}'.format("[C] Delete Announcement Post"))
        print('{:>92}'.format("[D] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        selection = input('{:>80}'.format("Enter your choice: ")).upper()
        if selection == 'A':
            clear()
            Post_Announcement()
            
        elif selection == 'B':
            clear()
            View_Announcement()
            
        elif selection == 'C':
            clear()
            delete_announcement()
            m.getch()
        elif selection == 'D':
            print("Going back to main menu...")
            m.getch()
            break
        else:
            print("\nInvalid choice. Please try again.")
            m.getch()

def View_Schedule():
    border2()
    print("\n\n\n")
    print('{:^170}'.format("Waste Collection Schedule"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>62}{'─'*46}┐" )
    print(f"{'':>62} {'DAY':<27} {'TIME':>11}      ")
    print(f"{'├':>62}{'─'*46}┤")

    for day, time in schedules.items():
        print(f"{"":>62} {day:<24} : {time:>11}   ")
        print(f"{'├':>62}{'─'*46}┤")

    print('{:^170}'.format("─" * 50))
    print("\n\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

def update_schedule():
    border2()
    print("\n\n\n")
    print('{:^170}'.format("Update Schedule:"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print('{:^68}'.format("Current Schedule:"))


    print(f"{'┌':>62}{'─'*46}┐" )
    print(f"{'':>62} {'DAY':<27} {'TIME':>11}      ")
    print(f"{'├':>62}{'─'*46}┤")

    for day, time in schedules.items():
        print(f"{"":>62} {day:<24} : {time:>11}   ")
        print(f"{'├':>62}{'─'*46}┤")

    print("\n")

    day = input('{:>62}'.format("Enter the day to update (e.g., Monday): ")).capitalize()

    if day in schedules:
        new_time = input('{:>62}'.format(f"Enter new time for {day} (e.g., 6:00am - 9:00am): "))
        schedules[day] = new_time
        print("\n")
        print('{:^170}'.format(f"Schedule for {day} updated successfully!"))

    else:
        print("\n\n")
        print('{:^170}'.format("Invalid day. Please try again."))

    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()  

def schedule():
    while True:
        clear()
        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste Collection Schedule"))
        print('{:^170}'.format("─" * 50))
        print("\n ")
        print('{:>90}'.format("[A] View Schedule"))
        print('{:>92}'.format("[B] Update Schedule"))
        print('{:>94}'.format("[C] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n")
        selection = input('{:>70}'.format("Enter your choice: ")).upper()

        if selection == 'A':
            clear()
            View_Schedule()
            m.getch()
        elif selection == 'B':
            clear()
            update_schedule()
            m.getch()
        elif selection == 'C':
            print("\n")
            print('{:^170}'.format("Going back to main menu..."))
            m.getch()
            break
        else:
            print("")
            print('{:^170}'.format("Invalid choice. Please try again."))
            m.getch()

def Update_Status_Report():
    border2()
    print("\n\n")
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
   
    print("─" * 178)
    print("\n\n")
    print('{:^170}'.format("Update Report Status"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    try:
        report_number = int(input('{:>60}'.format("Enter the report number to update (0 to exit): "))) - 1
        if report_number == -1:
            print('{:^170}'.format("Exiting update operation..."))
            return
            
        elif 0 <= report_number < len(reports):
            Time, Name_Reporter, Location, Issue, Status = reports[report_number].strip().split("|")
            new_status = input('{:>67}'.format("Enter new status (e.g.,[R] Resolved, [I] In Progress): ")).upper()
            if new_status == "R":
                new_status = "Resolved"
            elif new_status == "I":
                new_status = "In Progress"
            else:
                print("\n\n")
                print('{:^170}'.format("Invalid status. Please enter [R] for Resolved or [I] for In Progress."))
                m.getch()
                return

            reports[report_number] = f"{Time}|{Name_Reporter}|{Location}|{Issue}|{new_status}\n"

            with open(Reports_File, 'w') as file:
                file.writelines(reports)

            print("\n")
            print('{:^170}'.format("Report status updated successfully!"))
            m.getch()

        else:
            print("\n")
            print('{:^170}'.format("Invalid report number."))
            m.getch()

    except ValueError:
        print("\n")
        print('{:^170}'.format("Invalid input. Please enter a valid number."))
        m.getch()

def Waste_report():
    clear()
    border2()
    print("\n\n")
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
    print("─" * 178)

    print("\n\n")
    print('{:>40}'.format("Select:"))
    print(f"{'┌':>56}{'─'*61}┐")
    print(f"{'│':>56} {'':<10}{'[A] Update Status':<24} {'[B] Exit':<25}│")
    print(f"{'└':>56}{'─'*61}┘")
    select = input('{:>47}'.format("Enter Choice: ")).upper()

    if select == 'A':
        clear()
        Update_Status_Report()
        Waste_report()
        m.getch()
    elif select == 'B':
        print("\n")
        print('{:^170}'.format("Exiting..."))
        return
        m.getch()
          
    else:
        print("\n")
        print("Invalid Choice../")
        m.getch()

def Menu():
    while True:
        os.system('cls')

        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste - Management System"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>92}'.format("[A] Waste Collection"))
        print('{:>88}'.format("[B] Announcement"))
        print('{:>84}'.format("[C] Schedule"))
        print('{:>93}'.format("[D] View Waste Report"))
        print('{:>82}'.format("[E] Logout"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        choice = input('{:>80}'.format("Enter Choice: ")).upper()

        if choice == 'A':
            clear()
            Waste_Collection()
            m.getch()
        elif choice == 'B':
            clear()
            Announcement()
            m.getch()
        elif choice == 'C':
            clear()
            schedule()
            m.getch()
        elif choice == 'D':  
            clear()
            Waste_report()
            m.getch()
        elif choice == 'E':
            print("Logging out...")
            m.getch()
            Main_menu.main()
        else:
            print("Invalid choice. Please try again.")
            m.getch()