#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''
import math
def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''

    a=int((len(input))/2)
    b=input[0:a]
    c=input[a:99]

    if input[a].isspace():
        e=a
    else:
        if input[a-1].isspace():
            e=a-1
        else:
            e=a
    if input[e].isspace():
        d=f"{b}\n{c}"
    else:
        d=f"{b}-\n{c}"
    print(d)
    return d

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"