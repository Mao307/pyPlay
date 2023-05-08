# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:21:48 2023

@author: Moawia
"""

def reverse(s):
    
    #simple function that reverse given string
    if len(s) == 1:
        return s
    else:
         first_char = s[0]
         rest_string = s[1:]
         rev_rest= reverse(rest_string)
         return rev_rest+ first_char
 

def isPalindrome(s) :
    
    #simple function is to check whether the string is a palindrome
        if len(s) ==0:
            return True
    
        first_char =s[0]
        last_char= s[-1]
        middle_char= s[1:-1]
        if first_char != last_char:
            return False
        elif first_char == last_char:
            
            return isPalindrome(middle_char)
    
  