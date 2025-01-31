def main():
    """
    Main function to analyze a book file and print a character frequency report.
    """
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    nums_count = get_num_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
   
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{nums_count} words found in the document")
    print()
    
    # Print character frequencies, ignoring non-alphabetic characters
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
        

def sort_on(d):
    """
    Sorting key function to sort characters by frequency in descending order.
    """
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """
    Converts a dictionary of character counts into a sorted list of dictionaries.
    """
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)  # Sort by frequency (highest first)
    return sorted_list
        

def get_num_words(text):
    """
    Counts and returns the number of words in the given text.
    """
    return len(text.split())
    

def count_characters(text):
    """
    Counts the occurrences of each character in the given text, case insensitive.
    """
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    """
    Reads and returns the content of the book file at the given path.
    """
    with open(path) as f:  # Explicitly specifying encoding
        return f.read()    

# Run the main function
main()
