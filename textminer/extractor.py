import re

def phone_numbers(text):
    phone_list = []
    ext_phone = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
    match = re.findall(ext_phone, text)

    print(match)

    for num in match:
        a_list = []
        a_list.append("(" + num[0] + ") " + num[1] + "-" + num[2])
        phone_list.append("".join(a_list))
        #phone_list.append(a_list)
    return phone_list
