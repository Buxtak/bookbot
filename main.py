def main ():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_read = read_book(frankenstein_path)
    words_in_book = words_count(frankenstein_read)
    frankenstein_characters = characters_count(frankenstein_read)
    sorted_characters = sorted(frankenstein_characters.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin Report of {frankenstein_path} ---")
    print(f"{words_in_book} words found in the document")
    
    for character, count in sorted_characters:
        print(f"the '{character}' character was found {count} times")



def characters_count(book):
    lowercased_book = book.lower()
    characters_dict = {}
    
    for character in lowercased_book:
        if character.isalpha():
            if character not in characters_dict:
                characters_dict[character] = 1
            else:
                characters_dict[character] += 1
    return characters_dict
        

def words_count(book):
    words = book.split()
    return len(words)



def read_book(path):
    with open(path) as f:
        book = f.read()
    return book

main()



