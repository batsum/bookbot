def get_num_words(text):
    num_words = len(text.split())
    return num_words
    
def get_num_chars(text):
    characters = {}
    for x in text.lower():
        if x not in characters:
            characters[x] = 1
        else:
            characters[x] += 1
    return characters 
        
def sort_on(items):
    return items["num"]

def sort_list(characters):
    char_list = []
    for x,y in characters.items():
        if x.isalpha():
            char_list.append({"char":x,"num":y})
    char_list.sort(reverse=True,key=sort_on)
    return char_list 