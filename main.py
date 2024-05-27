import sys

file_path = "books/frankenstein.txt"


def main():
    file_contents = read_file(file_path)
    words = count_words(file_contents)
    letters = count_letters(file_contents)
    return file_contents, words, letters

    
def read_file(file_path):
    with open(file_path, 'r') as f:
        file_contents  = f.read() 
    return file_contents
    
def count_words(file_contents: str):
    count = file_contents.split()
    return len(count)

def count_letters(file_contents):
    letter_counts = {}
    for letter in file_contents.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def sort_on(dict: dict):
    return dict.values()

def generate_report(file_contents):
    words_count = count_words(file_contents)
    letters_count = count_letters(file_contents)
    print(f"Total words in the file: {words_count}")
    print("Letter counts:")
    for letter, count in sorted(letters_count.items()):
        print(f" The '{letter}' character was found {count} times")


done = False
while not done:
    choice = input("Enter 'words' to count words, 'letters' to count letters, enter 'report' to generate report, or 'file' to print file contents: ")

    if choice == 'words':
        file_contents = read_file(file_path)
        words = count_words(file_contents)
        print(words)
    elif choice == 'letters':
        file_contents = read_file(file_path)
        letters = count_letters(file_contents)
        print(letters)
    elif choice == 'file':
        file_contents = read_file(file_path)
        print(file_contents)
    elif choice == "report":
        file_contents = read_file(file_path)
        generate_report(file_contents)
    else:
        print("Invalid choice")

    done_choice = input("Are you done? (y/n) ")
    if done_choice.lower() == 'y':
        done = True
        sys.exit("Thank You For Using BookBot!!")
    
if __name__ == "__main__":
    sys.exit(main())


