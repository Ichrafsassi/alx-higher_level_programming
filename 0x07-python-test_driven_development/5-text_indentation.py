#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chs = ['.', '?', ':']
    new_txt = ""

    txt_len = len(text)
    for i in range(txt_len):
        if text[i] == ' ':
            if new_txt == "" or new_txt[-1] == "\n":
                continue
            new_txt += text[i]
        elif text[i] in chs:
            new_txt += text[i] + "\n\n"
        else:
            new_txt += text[i]
    print(new_txt, end="")
