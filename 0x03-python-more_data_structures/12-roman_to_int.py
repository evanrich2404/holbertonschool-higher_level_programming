#!/usr/bin/python3
def roman_to_int(roman_strings:str)-> int:
    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman_strings)):
        if i > 0 and roman_to_int_dict[roman_strings[i]]
        > roman_to_int_dict[roman_strings[i - 1]]:
            result += roman_to_int_dict[roman_strings[i]]
             - 2 * roman_to_int_dict[roman_strings[i - 1]]
        else:
            result += roman_to_int_dict[roman_strings[i]]
    return result
