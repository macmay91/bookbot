def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        
    numbers = word_count(text)
    print(numbers)
    characters = character_count(text)

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
    
    print(d)

    for letter in text_file:
         try:
            l_case_letter = letter.lower()
            d[l_case_letter] += 1
         except:
              pass
    
    print(d)





if __name__ == "__main__":
    main()