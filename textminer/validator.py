import re

def binary(text):
    if re.search(r"^[0|1]+$", text):
        return True
    else:
        return False


def binary_even(text):
    if re.search(r"0$", text):
        return True
    else:
        return False


def hex(text):
    if re.search(r"^[0-9A-F]+$", text):
        return True
    else:
        return False


def word(text):
    if re.search(r"^[0-9-]*[A-Za-z-]+$", text):
        return True
    else:
        return False


def words(text, count=0):
    word_list = text.split(" ")
    bool_list = []
    for i in word_list:
        value = word(i)
        bool_list.append(str(value))
    if count == 0 and "False" not in bool_list:
        return True
    elif "False" not in bool_list and count == len(word_list):
        return True
    else:
        return False


def phone_number(text):
    if re.search(r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})", text):
        return True
    else:
        return False

def money(text):
    if re.search(r"^^\$((\d{1,3}(,\d{3})*)|\d+)(\.\d{2})?$", text):
        return True
    else:
        return False

def zipcode(text):
    if re.search(r"^\d{5}(-?\d{4})?$", text):
        return True
    else:
        return False


def date(text):
    pass
