def main():
    path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        text = f.read()
        
    numbers = word_count(text)
    characters = character_count(text)
    character_list = ordered_list(characters)

    print_report(path, numbers, character_list)




def word_count(text_file):
        words = text_file.split()
        count = 0

        for x in words:
             count+= 1
        
        return count

def character_count(text_file):
    d = {}
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        d[letter] = 0
    
    

    for letter in text_file:
         try:
            l_case_letter = letter.lower()
            d[l_case_letter] += 1
         except:
              pass
    
    return d
    
    
def ordered_list(character_count):
     character_list = []

     for x, y in character_count.items():
         character_list.append({"letter": x, "num": y})
    
     character_list.sort(reverse=True, key=sort_on)
    
     return character_list

def print_report(book_path, words, character_list):
     
     print(f"--- Begin report of {book_path} ---")
     print(f"{words} words found in the document")
     print()

     for count in character_list:
          print(f"The '{count['letter']}' character was found {count['num']} times")
     print("--- End report ---")

def sort_on(dict):
     return dict["num"]


if __name__ == "__main__":
    main()