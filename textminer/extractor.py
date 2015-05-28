import re

def phone_numbers(text):
    phone_list = []
    ext_phone = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
    match = re.search(ext_phone, text)
    for i in match.groups():
        a_list = []
        a_list.append("(" + match.groups()[0] + ") ")
        a_list.append(match.groups()[1] + "-" + match.groups()[2])
    phone_list.append("".join(a_list))
    return phone_list
