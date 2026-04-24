# -*- coding: utf-8 -*-
def pig_it(text):
    # Split input text into a list of words
    words = text.split()
    
    # Iterate over words by index to modify them in-place
    for s in range(len(words)):
        string = words[s]
        """
            If the first character is a letter, apply Pig Latin transformation
            Move the first letter to the end and append "ay"
            Punctuation marks (e.g., "!", "?") are left unchanged
        """
        if string[0].isalpha():
            words[s] = words[s][1:] + words[s][0] + "ay"
    
    # Build the final string with spaces between words
    resault = ''
    for s in words:
        resault += s + " "
    
    # Remove trailing space and return result
    return resault.strip()
        
    return resault.strip()
