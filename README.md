# BookBot

BookBot is a simple Python program that analyzes a text file, counts the number of words, and calculates the frequency of each character in the text. This program is designed to work with any book or text file.

## Features

- Reads a text file and analyzes its content
- Counts the total number of words in the document
- Counts and sorts character frequencies (case-insensitive)
- Ignores non-alphabetic characters in the frequency report

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/rokib97/bookbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd bookbot
   ```
3. Ensure you have Python installed (version 3.x recommended).

## Usage

Run the script using the following command:

```sh
python main.py
```

## File Structure

```
bookbot/
│── books/
│   └── frankenstein.txt  # Sample book text file
│── main.py               # Main script to run the analysis
│── README.md             # Documentation file
```

## Example Output

```
--- Begin report of books/frankenstein.txt ---
78912 words found in the document

The 'e' character was found 6789 times
The 't' character was found 5432 times
...
--- End report ---
```

## License

This project is open-source and available for educational purposes.

## Author

Developed by [Rokib](https://github.com/rokib97).
