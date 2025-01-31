def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        nums_count = get_num_words(file_content)
        chars_dict = count_characters(file_content)
        print(chars_dict)
        
def get_num_words(text):
    return len(text.split())
    
def count_characters(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
main()