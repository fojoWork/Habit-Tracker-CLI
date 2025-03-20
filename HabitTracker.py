import os
#Displays a menu the user can navigate
def Menu():
    print("📅 HABIT TRACKER CLI")
    ModeSelected = input("1. Add habit\n" + "2. Mark habit as done\n" + "3. View habit and score streaks\n\n" + "4. Exit\n" + "Enter your choice: \n")
    if ModeSelected == '1':
        AddHabit()
        input("Press enter to return to menu\n")
        Menu()
    elif ModeSelected == '2':
        RmHabit()
        input("Press enter to return to menu\n")
        Menu()
    elif ModeSelected == '3':
        ViewHabit()
        input("Press enter to return to menu")
        Menu()

#Functions for adding habits, marking habits as done, and viewing habits
def AddHabit():
    habitName = input("Habit Name?: \n")
    with open("habits.txt", "a") as file:
        file.write(habitName + "\n")
        #Save Confirmation
        print('\nSaved ' + '"' + habitName + '"' + " as your habit name!")


def ViewHabit():
    with open("habits.txt", "r") as file:
        habits = file.readlines()
        if habits:
            for habit in habits:
                print(f"- {habit.strip()}")
        else:
            print("No habits found. Add some to get started!")
def RmHabit():
    habit_to_remove = input("Enter the habit to remove: ").strip().lower()

    with open("habits.txt", "r") as file:
        habits = file.readlines()

    new_habits = [habit for habit in habits if habit.strip().lower() != habit_to_remove]

    if len(new_habits) == len(habits):
        print("\n Habit not found.")
    else:
        with open("habits.txt", "w") as file:
            file.writelines(new_habits)
        print(f"\nRemoved: {habit_to_remove}")

        

#Start menu
Menu()
