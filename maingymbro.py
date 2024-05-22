def main_menu():
    exercises = {"Bröst": ["Bänkpress", "Hantelpress", "Flyes"],
                 "Rygg": ["Rodd", "Marklyft", "Pull-ups"],
                 "Ben": ["Knäböj", "Utfall", "Marklyft"],
                 "Armar": ["Bicepscurl", "Tricepsextension", "Hantelcurl"]}  
    
    workouts = {}
    while True:
        print("\nHello! What do you want? \nHere are some choices of input.")
        print("[1] Input new workout.\n[2] List old inputs.")
        print("[3] Get arms like Fred.\n[4] Exit")

        try:
            user_input = int(input("Enter number here:"))

            if user_input == 1:
                print("Okay, what muscle group have you focused on today? Here are some choices:")
                for muscle_group, exercises_list in exercises.items():
                    exercises_cleaned = ", ".join(exercises_list).replace("[", "").replace("]", "").replace("'", "")
                    print(f"{muscle_group}: {exercises_cleaned}")
                muscle_group = input("What muscle group do you want to add to? ")
                if muscle_group in exercises:
                    print("Selected muscle group:", muscle_group)
                    print("Available exercises:", exercises[muscle_group])
                    
                else:
                    print("Invalid muscle group!")
                
            elif user_input == 2:
                print_saved_data(exercises, workouts)
            elif user_input == 3:
                print("Lägg ner grabben, det går inte")
            elif user_input == 4:
                break
            else:
                print("Enter a valid number from the menu!")
        except ValueError:
            print("Enter a valid number from the menu!")


def print_saved_data(exercises, workouts):
    print("\nSaved Exercises:")
    for muscle_group, exercise_list in exercises.items():
        for exercise in exercise_list:
            print(f"Muscle group: {muscle_group}, Exercise: {exercise}")

    print("\nSaved Workouts:")
    for index, workout in enumerate(workouts, start=1):
        print(f"{index}. {workout}")


main_menu()
