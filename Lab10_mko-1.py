"""
Program Name: Lab10_mko1-1.py
Name (Author): Michael Ko
Professor: Travis Burke
Purpose: The purpose of this is to create an OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. The program will count the frequency of every word in the selected file and print an alphabetical report. 
Starter Code: The text files princess_mars.txt, Tarzan.txt, treasure_island.txt, and monte_cristo.txt. I also used some code/concepts introduced in the Weekly Lecture (October 1st).
Date: 10/04/2026

Note: The letters in parenthesis represent my attemot of following along the instructions of Lab 3 - Programming Assignment (Chapter 10)
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        """Takes the filepath (as a string) and stores it as a private pathlibrary"""
        self.__path = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Reads the file, cleans text, counts word frequencies."""
        try:
            """(b) Checks for the file"""
            if not self.__path.exists():
                print("Error: File does not exist.")
                return False

            """(d) Translation table to remove all punctuation from each line"""
            translator = str.maketrans("", "", string.punctuation)

            """c) Reads file line by line"""
            with self.__path.open("r", encoding="utf-8") as file:
                for line in file:
                    """(e) Converts each line to all lowercase"""
                    clean_line = line.lower().translate(translator)

                    """(f) Splits each line into words"""
                    words = clean_line.split()

                    """(f) Updates counts of words in the internal frequencies dictionary"""
                    for word in words:
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            
            """(g) True if processing was successful. If a FileNotFoundError occurred, False"""
            return True
    
        except FileNotFoundError:
            print("FileNotFoundError: Could not open the file.")
            return False

    def print_report(self):
        """Prints alphabetical word-frequency result/report/prints the results"""
        print("\n--- WORD FREQUENCY REPORT ---")
        for word in sorted(self.__frequencies.keys()):
            print(f"{word}: {self.__frequencies[word]}")
        print("------------------------------\n")

def main():
    """Acts as the 'driver' for the program. Shows the menu, gets user input, runs WorldAnalyzer class. Dictionary of 4 files"""
    
    BASE_DIR = Path(__file__).parent

    files = {
    "1": BASE_DIR / "Tarzan.txt",
    "2": BASE_DIR / "monte_cristo.txt",
    "3": BASE_DIR / "princess_mars.txt",
    "4": BASE_DIR / "treasure_island.txt"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("\nPlease select a file to analyze:")
        print("1. Tarzan")
        print("2. Monte Cristo")
        print("3. Princess Mars")
        print("4. Treasure Island")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "5":
            print("Exiting program. Goodbye!")
            break

        if choice not in files:
            print("Invalid choice. Please try again by selecting a number from 1-5.")
            continue

        filepath = files[choice]

        analyzer = WordAnalyzer(filepath)

        if analyzer.process_file():
            analyzer.print_report()

"""Program starts if the file is run directly."""
if __name__ == "__main__":
    main()