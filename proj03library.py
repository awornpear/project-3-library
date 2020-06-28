# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:53:54 2020

@author: Benny
"""


#Project 3

#Constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

#Functions

#is_alpha
def is_alpha(str):
    x= True
    for i in str:
        if i not in ASCII_LOWERCASE and i not in ASCII_UPPERCASE:
            x= False
    if x== True:
        return True
    else:
        return False

#is_digit
def is_digit(str):
    if str in DECIMAL_DIGITS:
        return True
    else:
        return False

#find_chr    
def find_chr(start_str, find_ch):
    if len(find_ch) != 1:
        return -1
    else:
        for i, ch in enumerate(start_str):
            if ch == find_ch:
                return i
    return -1


#to_lower   
def to_lower(start_str):
    output_str = ''
    for ch in start_str:
        if ch in ASCII_UPPERCASE:
            index= find_chr(ASCII_UPPERCASE, ch) 
            output_str += ASCII_LOWERCASE[index]
        else:
            output_str += ch
    return output_str

#to_upper
def to_upper(start_str):
    output_str= ''
    for ch in start_str:
        if ch in ASCII_LOWERCASE:
            index= find_chr(ASCII_LOWERCASE, ch)
            output_str += ASCII_UPPERCASE[index]
        else:
            output_str += ch
    return output_str

#find_str
def find_str(str1, str2):
    if str2 not in str1 or len(str2) > len(str1):
        return -1
    else:
        for i, ch in enumerate(str1):
            if ch== str2[0]:
                if str1[i:i+len(str2)] == str2:
                    return i
#replace_chr
def replace_chr(str1, str2, str3):
    str4 = ''
    if len(str2) != 1 or len(str3) != 1:
        return -1
    elif str2 not in str1:
        return -1
    else: 
        for i, ch in enumerate(str1):
            if ch == str2:
                str4 = str4 + str3
            else:
                str4 = str4 +ch
                
        return str4

#replace_str
def replace_str(str1, str2, str3):
    str4 = ''
    if str2 not in str1:
        return str1
    elif str2 == '':
        return str3 + str1 + str3
        
    else: 
        for i, ch in enumerate(str1):
            if ch == str2[0]:
                if str1[i: i+ len(str2)] == str2:
                    str4 = str1[:i] + str3 + str1[i +len(str2):]       
        return str4
    
    
