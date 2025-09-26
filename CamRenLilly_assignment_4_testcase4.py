# Copilot was used to help assign the float variable correctly
student_name = "Cam'Ren Lilly"
current_gpa = 3.26
study_hours = 22
social_points = 28
stress_level = 48

print("Welcome these are your starting stats:")
print(f"Name: {student_name}")
print(f"GPA: {current_gpa:.2f}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress level: {stress_level}")
# Course loads
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
# Input value for the course loads
choice = input("Your choice: ")

if choice == "A":
    print("You have chosen the light course load otion")

    current_gpa = 3.76
    stress_level -= 9
    social_points += 9
    
    print(f" GPA: {current_gpa}")
    print(f" Stress: {stress_level}")
    print(f" Social points: {social_points}")
    print()
    
    if current_gpa >= 3.5:
        print("Congrats!,you've made the chancellor's list this is one of the highest achievements you can get.")

elif choice == "B":
    print("You have chosen the standard couse load option")
    current_gpa = 3.52
    stress_level += 3
    social_points += 2

    print(f" GPA: {current_gpa}")
    print(f" Stress: {stress_level}")
    print(f" Social points: {social_points}")

    if current_gpa >= 3.5:
        print("Congrats!, you've made the deans list")

elif choice == "C":
    print("You have chosen the heavy course load option")

    current_gpa = 3.19
    stress_level += 12
    social_points -= 8

    print(f" GPA: {current_gpa}")
    print(f" Stress: {stress_level}")
    print(f" Social points: {social_points}")

    if current_gpa >= 3.5:
        print("You have earned a gpa of 3.5 or higher!. And you have made the Dean's list!.")
    else:
        print("You didn't make the Dean's list but there's always next semester")

else:
    print("Invalid choice, game over.")

#Decision 2
print("\nPick your study option:")
print("Options: Programming, Math, English, History")
study_choice = input("Enter your choice: ")
study_options = ["Programming", "Math", "English", "History"]

if study_choice in study_options:
    print(f"You chose to study {study_choice} this choice increases your gpa by striving for academic excellence")
    current_gpa += .2
elif study_choice not in study_options:
    print("You chose to skip studying and instead went to a party.")
    print("Your gpa, social points, and stress levels will be changed upon this decision")
    current_gpa -= .5
    social_points += 18
    stress_level -= 10
else:
    print("Invalid choice, Stats remain unchanged")
    

print("\n Current stats after picking a study option:")
print(f"GPA: {current_gpa:.2f}")
print(f"Social points: {social_points}")
print(f"Stress level: {stress_level}")

#decision 3

chancellors_list = 3.75
deans_list = 3.25
stress_limit = 55

if current_gpa >= chancellors_list:
    if stress_level <= 45:
        if social_points >=35:
            print("Outcome: You've had a great semester, You've made it on the chancellors list while also not being burntout and while also having a balanced social life.")
        else:
                print("Outcome: You've done well academically but you need to be more social.")
    else:
        print("Outcome: You've made the chancellors list but your stress is over the limit, you need to take breaks more often.")
elif current_gpa >= deans_list:
    if stress_level <= 55:
        if social_points >= 45:
            print("Outcome: You're doing well, you made the dean's list  your stress isn't too bad and you've had a decent social life.")
        else:
            print("Outcome: Your academics are going well but your socially akward, you need to put yourself out there.")
    else:
        print("Outcome: your academics are going well but your stress is too high, you need better habits to prevent burnout.")
else:
    if stress_level > 55:
        print("Outcome: You're struggling your gpa isn't where it should be and your stress is through the roof, look for support.")
    elif social_points >=35:
        print("Outcome: Your social points are at its peak but your academics are at its lowest, time to lock in.")
    else:
        print("Your academics are low, your social points are low, and your stress is relatively high you are bound to be placed on academic probation.")


if stress_level is stress_limit:
    print("You've reached the limit for your stress and have reached burnout.")
elif stress_level is not stress_limit:
    print("You're below the limit, keep managing your stress to prevent burnout.")

print("Final Stats:")
print(f"GPA: {current_gpa:.2f}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress level: {stress_level}")