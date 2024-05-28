import sys
import argparse
from openai import OpenAI
from collections import Counter
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set your OpenAI API key from the environment variable

# Function to read the file content
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)

# Function to count words in the file content
def count_words(file_contents):
    count = file_contents.split()
    return len(count)

# Function to count letters in the file content
def count_letters(file_contents):
    letter_counts = {}
    for letter in file_contents.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

# Function to generate a report of word and letter counts
def generate_report(file_contents):
    words_count = count_words(file_contents)
    letters_count = count_letters(file_contents)
    print(f"Total words in the file: {words_count}")
    print("Letter counts:")
    for letter, count in sorted(letters_count.items()):
        print(f"The '{letter}' character was found {count} times")

# Function to count unique words
def count_unique_words(file_contents):
    words = file_contents.split()
    unique_words = set(words)
    return len(unique_words)

# Function to find the longest word
def find_longest_word(file_contents):
    words = file_contents.split()
    longest_word = max(words, key=len)
    return longest_word

# Function to find the most common word
def find_most_common_word(file_contents):
    words = file_contents.split()
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0]
    return most_common_word

# Function to answer questions using OpenAI's GPT model
def answer_question(file_contents, question):
    response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context: {file_contents}\n\nQuestion: {question}\nAnswer:"}
    ],
    max_tokens=3000)
    answer = response.choices[0].message.content.strip()
    return answer

# Function to handle the CLI logic for a single action
def handle_action(action, file_contents, question=None):
    if action == 'words':
        words = count_words(file_contents)
        print(f"Total words: {words}")
    elif action == 'letters':
        letters = count_letters(file_contents)
        print("Letter counts:")
        for letter, count in sorted(letters.items()):
            print(f"The '{letter}' character was found {count} times")
    elif action == 'file':
        print(file_contents)
    elif action == 'report':
        generate_report(file_contents)
    elif action == 'unique_words':
        unique_words = count_unique_words(file_contents)
        print(f"Total unique words: {unique_words}")
    elif action == 'longest_word':
        longest_word = find_longest_word(file_contents)
        print(f"The longest word: {longest_word}")
    elif action == 'common_word':
        most_common_word = find_most_common_word(file_contents)
        print(f"The most common word: '{most_common_word[0]}' occurred {most_common_word[1]} times")
    elif action == 'ask_question':
        if not question:
            print("Error: A question must be provided for the 'ask_question' action.")
        else:
            answer = answer_question(file_contents, question)
            print(f"Answer: {answer}")
    else:
        print(f"Unknown action: {action}")

# Main function to handle the CLI logic
def main():
    parser = argparse.ArgumentParser(description="A CLI tool to analyze text files")
    parser.add_argument('file_path', type=str, help="Path to the text file")
    args = parser.parse_args()

    file_contents = read_file(args.file_path)

    while True:
        action = input("Enter action (words, letters, file, report, unique_words, longest_word, common_word, ask_question, or exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the CLI. Thank you!")
            break
        question = None
        if action == 'ask_question':
            question = input("Enter your question: ").strip()
        handle_action(action, file_contents, question)

# Entry point for the script
if __name__ == "__main__":
    main()
