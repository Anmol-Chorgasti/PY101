dictionary = {"first": [1]}
num_dict = dictionary.copy()
num_dict["first"].append(2)
print(dictionary["first"]) #[1,2]


"""
question4
"""

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) == 4:
        while len(dot_separated_words) > 0:
            word = dot_separated_words.pop()
            if not is_an_ip_number(word):
                break
        return True

    return False

print(is_dot_separated_ip_address("4.5.5"))
print(is_dot_separated_ip_address("1.2.3.4.5.6"))
print(is_dot_separated_ip_address("10.4.5.11"))


