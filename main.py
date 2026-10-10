"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = cost_per_semester(annual_cost) /  credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER
    return class_cost

def cost_of_skipped_classes(annual_cost, credits, skipped_classes):
    """Give back the cost of skipped CS 1430 """
    skipped_class_cost = cost_per_class(annual_cost, credits) * skipped_classes
    return skipped_class_cost

def cost_of_repeating_course(annual_cost, credits):
    """Give back the cost of repeating a 3 credit course."""
    repeat_cost = (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) * SEMESTERS_PER_YEAR
    return repeat_cost

def credit_load_comparision(annual_cost, credits):
    """Give back the cost comparison of different credit loads between 12 and 18 credits"""
    for credit_load in range(12, 19):
        cost_per_credit_this = cost_per_credit(annual_cost, credits) * credit_load
        print(f"Cost per credit for {credit_load} credits: ${cost_per_credit_this:.2f}")

def four_year_projection(annual_cost, increase):
    """Give back the four-year cost projection with an annual increase"""
    total_cost = 0
    yearlyCost = annual_cost
    for year in range(4):
        total_cost += cost_per_semester(yearlyCost)
        yearlyCost *= (1 + increase)
    return total_cost




# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year of college: "))
    credits = int(input("Enter the number of credits you will be taking this semester: "))
    print("THE COST OF COLLEGE:")
    print("1 - Per Semsester")
    print("2 - Per Month")
    print("3 - Per Class Day")
    print("4 - Per Credit")
    print("5 - Per CS 1430 Class")
    print("6 - Cost of Skipped Classes")
    print("7 - Repeating a 3 Credit Course")
    print("8 - Credit Load Comparison")
    print("9 - Four-year Projection")
    print("Q - Quit")
    while True:
        # Show your menu here.
        choice = input("Choose an option: ")
        if choice == "1":
            print(f"A Semester of College Costs: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"A Month of College Costs: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"A Full Class Day of College Costs: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"A Single Credit in College Costs: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"A Single, 50 Minute CS1430 Class Costs: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            skipped_classes = int(input("Enter the number of CS 1430 classes you skipped: "))
            print(f"The Cost of Skipping {skipped_classes} CS 1430 Classes is: ${cost_of_skipped_classes(annual_cost, credits, skipped_classes)} of missed classes")
        elif choice == "7":
            print(f"The cost of repeating a 3 credit course is: ${cost_of_repeating_course(annual_cost, credits):.2f}")
        elif choice == "8":
            credit_load_comparision(annual_cost, credits)
        elif choice == "9":
            increase = float(input("Enter the annual cost increase per year: "))
            print(f"The four-year cost projection is ${four_year_projection(annual_cost, increase):.2f} with a {increase*100:.2f}% annual increase in price")
        if choice == "Q":
            break

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
