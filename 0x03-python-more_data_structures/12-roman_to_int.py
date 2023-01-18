#!/usr/bin/python3

def roman_to_int(roman_strings):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_strings)
    roman_list.reverse()
    result = 0
    if roman_strings == '' or roman_strings == None or roman_strings != str:
        return 0
    else:
        for i in range(len(roman_list)):
            if i == 0:
                result += roman_dict[roman_list[i]]
            elif roman_dict[roman_list[i]] < roman_dict[roman_list[i - 1]]:
                result -= roman_dict[roman_list[i]]
            else:
                result += roman_dict[roman_list[i]]
    return result
