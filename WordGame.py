"""
Zain Khalbous,
engineering 1
ENGINEER 1P13: Integrated Cornerstone Design Projects in Engineering
Sam Scott, Fall 2024
This program is containing 3 function to display the word guess game

"""


"""Loading and Choosing Words"""

import random

def load_words(filename):
    """This function open a file and create list from it, each line into list, the return a list 
    if file is in wrong length, bad characters or empty it returns Fales filename=>the file that would be opened
    """
    
    
    file=open(filename)
    
    string_list=[] #empty list to append the lists inside
    

    for word in file: #for loop to go through each line and append it to the string_file

        word = word.strip()
        
        string_list.append(word)
        
    
    
    file.close()

    for word in string_list:#for loop to find if this is a bad character
        word=str(word)
        for char in word:
            char=str(char)     
            if char.isalpha()==False:
                
                return False 
    
    for i in range(len(string_list)):#if file contain words no in same lengnth
        j=1
        if len(string_list[i])!=len(string_list[j]):
            return False
        j+=1
    
    if string_list==[]: #if file is empty then qreturn False
        return False

    return string_list #return the list from the file


def choose_word(word_list):
    """This function would return random word from the list and if list is empty it return False
    word_list=> list of word that random index would be choosen from it
    """
    
    i = random.randint(0, len(word_list)-1) #choose random index
    
    if word_list==[]: #if list empty return False
        return False
    
    return i #return interger (index)


"""Tracking the Letters Used"""

def update_letters(letters, target, guess):
    """This function would take guess from user and target word,
    it will update the letter list from True to False if the guess word has no corresponding entry from target
    letters=> is list of boolen for the index of the letters  target=> the word that we compare its letters with guess letters  guess=> user word  
    
    """
    
    for letter in guess:#for loop to detemine if guess letters is in target letters then change the index of letter list from true to false if letter does not exist in target
        i=0
            
        if letter[i] not in target:
            k=ord(letter[i])-ord("a") #k is refer to the index number in alphaptic order eg. letter[i]=a k=ord(letter[i])-ord("a")-->97 ===== 97-97 k=0 so k is the first index 
            letters[k]=False
          
        i+=1
        
      
"""Evaluating a Guess"""

def score_guess(guess, target, words):
    
    """This function take a guess from user then evaluate it based on the target word from words list 
    it would return "?"---misplaced  "*"---correct position  "_"---not in target False---wrong size or not in the words list 
    guess=> user word target=> the word that guess is being compared with based target letter's position.
    """
    guess= guess.lower().strip()
    if guess not in words or len(guess)!=len(target): #if guess is not in words list or length of guess is different than target 
        
        return False
    
    
    score='' #intial state for word
    for i in range(len(guess)):
        
        if guess[i]==target[i]: #"*"--- if correct position 
            
            score+='*'
            
        elif guess[i] in target: #"?"---if in target but misplaced
            
            score+="?"
            
        else: #if it is not in target
            score+="_"
            
    return score #return the hole score of the word


 

        

                
                
        
        
    
    
    

    