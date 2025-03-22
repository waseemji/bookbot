def get_word_count(text):
    words = text.split()
    return len(words)

def get_dict(text):
    mt_dict = {}
    for letter in text:
        letter = letter.lower()
        if(letter not in mt_dict):
            mt_dict.update({letter:1})
        else :
            mt_dict[letter] += 1

    return mt_dict


def sort_on(dict):
    return dict["count"]

def sorted_charactor_count(text):
    dict = get_dict(text)
    mt_list=[]
    for k,v in dict.items():
        mt_list.append({"char":k,"count":v})
    mt_list.sort(reverse=True,key=sort_on)
    return mt_list
