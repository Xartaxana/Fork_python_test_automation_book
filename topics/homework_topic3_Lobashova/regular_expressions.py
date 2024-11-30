import re

#Task 1: Define if a string contains the required characters. E.g. if '7865serS3' includes '583' - True; '973' - False
my_string = "7865serS3"
case1 = "583"
case2 = "973"

def contains_char(chars, string):
    for ch in chars:
        match = re.search(re.escape(ch), string)
        if not match:
            return False
    return True

print (contains_char(case1, my_string))
print (contains_char(case2, my_string))

#Task 2: Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'
my_string2 = "75WseTrS3"

def num_of_upper_letters(string):
    return len(re.findall('[A-Z]', string))

print(num_of_upper_letters(my_string))
print(num_of_upper_letters(my_string2))

#Task 3: Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;

def contains_upper_then_lower(string):
    if re.search('[A-Z][a-z]', string):
        return True
    else: return False

print(contains_upper_then_lower(my_string))
print(contains_upper_then_lower(my_string2))