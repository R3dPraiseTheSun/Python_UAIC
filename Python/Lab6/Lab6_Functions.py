import re
from typing import List
import os

def extract_words(input_text: str) -> List[str]:
    """
    Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
    alpha-numeric characters.
    """
    return re.findall(r"\w+", input_text)


def ex_2(regex: str, input_text: str, x: int) -> List[str]:
    """
    Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns
    those long-length x substrings that match the regular expression.
    """
    return [i for i in re.findall(regex, input_text) if len(i) == x]


def ex_3(input_text_list: list, regex_list: List[str]) -> List[str]:
    """
    Write a function that receives two parameters: a list of strings and a list of regular expressions.
    The function will return a list of the strings that match on at least one regular expression from the list given as parameter.
    """
    match_list = []
    for input_text in input_text_list:
        for regex_el in regex_list:
            found_elements = re.findall(regex_el, input_text)
            for element in found_elements:
                if element not in match_list:
                    match_list.append(element)
    return match_list


def ex_4(path: str, attributes: dict) -> List[str]:
    """
    Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those
    elements that have as attributes all the keys in the dictionary and values the corresponding values.
    """
    match_list = []
    with open(path, "r") as file:
        xml_data = file.read()
        search_string = r"(<(\w+)" + r"".join(
            [" {key}=\"{value}\"".format(key=key, value=value) for key, value in attributes.items()]
        ) + r">[^</\2>]*</\2>)"
        #print(search_string)
        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    return match_list


def ex_5(path: str, attributes: dict) -> List[str]:
    """
    Write another variant of the function from the previous exercise that returns those elements that have at least one
    attribute that corresponds to a key-value pair in the dictionary.
    """
    match_list = []
    with open(path, "r") as file:
        xml_data = file.read()
        search_string = r"(<(\w+) [^>]*(" + r"|".join(
            ["{key}=\"{value}\"".format(key=key, value=value) for key, value in attributes.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
        #print(search_string)
        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    return match_list


def censor_text(input_text: str) -> str:
    input_text = input_text.group(0)

    return "".join([input_text[i] if i % 2 == 0 else "*" for i in range(len(input_text))])


def ex_6(input_text: str) -> str:
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
    means replacing characters from odd positions with *.
    """
    return re.sub(r"\b[aeiou](\w*[aeiou])?\b", censor_text, input_text)


def get_days_from_month_regex(year: str, month: str) -> str:
    days_per_month = [
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|1\d|2[0-8])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])"
    ]
    try:
        if int(year) % 4 == 0:
            days_per_month[1] = r"(0[1-9]|1\d|2[0-9])"
        return days_per_month[int(month) - 1]
    except Exception as e:
        raise SystemError(e)


def get_control_digit(digits: str) -> str:
    checksum_number = "279146358279"
    checksum = 0
    for i, j in zip(checksum_number, digits):
        checksum += int(i) * int(j)
    checksum %= 11
    if checksum == 10:
        checksum = 1
    return str(checksum)


def ex_7(input_text: str) -> bool:
    """
    Verify using a regular expression whether a string is a valid CNP.
    """
    match_first_digit = r"[1-8]"
    match_year = r"\d{2}"
    match_month = r"(0[1-9]|1[0-2])"
    match_day = get_days_from_month_regex(input_text[1:3], input_text[3:5])
    match_county = r"(0[1-9]|[1-3]\d|4[0-6]|5[1-2])"
    random_digits = r"(00[1-9]|0[1-9]\d|\d\d\d)"
    control_digit = get_control_digit(input_text[:-1])
    regex_string = r"^" + match_first_digit + match_year + match_month + match_day + match_county + random_digits + control_digit + r"$"
    #print(regex_string)
    return bool(re.match(regex_string, input_text))


def ex_8(path: str, regex: str) -> List[str]:
    """
    Write a function that recursively scrolls a directory and displays those files whose name matches
    a regular expression given as a parameter or contains a string that matches the same expression.
    Files that satisfy both conditions will be prefixed with ">>".
    """
    match_list = []
    try:
        for root, d, f in os.walk(path):
            for i in f:
                file_path = os.path.join(root, i)
                bool_1 = re.match(regex, file_path)
                bool_2 = re.match(regex, open(file_path, "r").read())
                if bool_1 and bool_2:
                    match_list.append(">>" + file_path)
                elif bool_1 or bool_2:
                    match_list.append(file_path)
    except Exception as e:
        SystemError(e)
    return match_list
