"""
CP1404 - Practical 10
wiki
This program asks for a search term to be entered and then the associate wikipedia link and a synopsis is provided
"""

import wikipedia


def main():
    page_search = input("Enter search term: ")
    while page_search != "":
        try:
            page = wikipedia.page(page_search, auto_suggest=False)
            print(page.title)
            print(page.url)
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            print("Please be more specific")
        page_search = input("Enter search term: ")


if __name__ == '__main__':
    main()
