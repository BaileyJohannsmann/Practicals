"""
CP1404 - Practical 7
Incomplete due to poor time management, difficulties and engineering exams
"""

import datetime
from Practicals.prac_07.project import Project
from operator import attrgetter
MENU = """Menu:
(L)oad projects
(S)ave projects
(D)isplay projects 
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
"""


def main():

    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_file()
        elif choice == "S":
            save_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid Menu choice")
        print(MENU)
        choice = input(">>> ").upper()


