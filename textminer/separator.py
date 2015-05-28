import re

def words(text):
    #re.search(r"^[0-9-]*[A-Za-z-]+$", text)
    word_list = re.split(r"\W+", text)
    return word_list


#Fails None test
def phone_number(text):
    phone_dict = {}
    ext_phone = r"(?:\(?(\d{3})\)?[\-\.]?\s*)?(\d{3})[\-\.]?(\d{4})"
    match = re.search(ext_phone, text)
    phone_dict["area_code"] = "{}".format(match.groups()[0])
    phone_dict["number"] = "{}-{}".format(match.groups()[1], match.groups()[2])
    return phone_dict


def money(text):
    money_dict = {}
    match = re.search(r"(^^\$)((\d{1,3}(,\d{3})*)|\d+)(\.\d{2})?$", text)
    money_dict["currency"] = "{}".format(match.groups()[0])
    money_dict["amount"] = "{}{}".format(match.groups()[1], match.groups()[4])
    return money_dict


def zipcode(text):
    zip_dict = {}
    match = re.search(r"(?:(\d{5})[-]?(\d{4})?)", text)
    zip_dict["zip"] = "{}".format(match.groups()[0])
    zip_dict["plus4"] = "{}".format(match.groups()[1])
    if zip_dict["plus4"] == "None":
        zip_dict["plus4"] = None
    return zip_dict
