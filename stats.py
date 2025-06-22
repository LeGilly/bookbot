def get_word_count(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

def get_character_count(book_text):
    new_dict = {}
    initial_count = 1
    for char in book_text.lower():
        if char not in new_dict:
            new_dict[char] = initial_count
        else:
            new_dict[char] += 1
    return new_dict

def get_sorted_list(unsorted_dictionary):
    new_list = []
    for entry in unsorted_dictionary:
        empty_dict = {}
        empty_dict["char"] = entry
        empty_dict["num"] = unsorted_dictionary[entry]
        new_list.append(empty_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]