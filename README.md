# Documentation for the BookBot Script
(I auto generated the documentation using an LLM)
## BookBot is my first project!

## Overview
The provided script, `BookBot`, reads a text file, counts the number of words and letters, and generates a report on letter frequencies. It offers an interactive menu to choose different operations such as counting words, counting letters, generating a report, and printing file contents.

## Code Components

### Imports
```python
import sys
```
- `sys`: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

### File Path
```python
file_path = "books/frankenstein.txt"
```
- `file_path`: Specifies the path to the text file (`frankenstein.txt`) which is to be read and analyzed.

### Main Function
```python
def main():
    file_contents = read_file(file_path)
    words = count_words(file_contents)
    letters = count_letters(file_contents)
    return file_contents, words, letters
```
- `main()`: The main function that reads the file, counts words, counts letters, and returns the results.

### Read File Function
```python
def read_file(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
    return file_contents
```
- `read_file(file_path)`: Reads the content of the file specified by `file_path` and returns it as a string.

### Count Words Function
```python
def count_words(file_contents: str):
    count = file_contents.split()
    return len(count)
```
- `count_words(file_contents)`: Splits the file content into words and returns the count of words.

### Count Letters Function
```python
def count_letters(file_contents):
    letter_counts = {}
    for letter in file_contents.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts
```
- `count_letters(file_contents)`: Counts the frequency of each letter in the file content and returns a dictionary with letters as keys and their counts as values.

### Sort On Function
```python
def sort_on(dict: dict):
    return dict.values()
```
- `sort_on(dict)`: Returns the values of the given dictionary. This function is currently unused in the script.

### Generate Report Function
```python
def generate_report(file_contents):
    words_count = count_words(file_contents)
    letters_count = count_letters(file_contents)
    print(f"Total words in the file: {words_count}")
    print("Letter counts:")
    for letter, count in sorted(letters_count.items()):
        print(f" The '{letter}' character was found {count} times")
```
- `generate_report(file_contents)`: Generates and prints a report showing the total word count and the frequency of each letter.

### Interactive Menu
```python
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
```
- The interactive menu allows the user to choose different operations:
  - `'words'`: Counts and prints the number of words in the file.
  - `'letters'`: Counts and prints the frequency of each letter in the file.
  - `'file'`: Prints the content of the file.
  - `'report'`: Generates and prints a detailed report.

### Script Entry Point
```python
if __name__ == "__main__":
    sys.exit(main())
```
- Ensures that the `main()` function runs when the script is executed directly.

## Usage
1. Ensure that the text file `frankenstein.txt` is located in the `books` directory.
2. Run the script.
3. Follow the interactive prompts to perform various operations on the file.
4. Exit the script by responding with 'y' when asked if you are done.

## Summary
This script is designed to perform basic text analysis on a given file. It provides an interactive way to count words, count letters, generate reports, and print file contents.