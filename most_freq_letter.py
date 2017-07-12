"""

https://py.checkio.org/mission/most-wanted-letter/solve/

You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.
Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105

"""


def checkio(text):

    # hash table to keep track of character count occurances
    # key is the ord() of the char, value is the count
    ord_occurance = {}
    
    # ['a':'z'] set count to 0 initially
    for i in range(ord('a'),ord('z')+1):
        ord_occurance[i]=0
    
    # track char occurances in lowercase
    delta = ord('a') - ord('A')
    for ch in text:
        if ord(ch) in range(ord('A'), ord('Z')+1):
            ch = chr(ord(ch) + delta)
            
        if ord(ch) in range(ord('a'), ord('z')+1):
            ord_occurance[ord(ch)] += 1
    
    # go through the hash table and find the largest count
    max_ord_letter = ord('z')
    max_cnt = 0
    for ord_letter, cnt in ord_occurance.items():
        
        if cnt == max_cnt:
            
            if ord_letter <= max_ord_letter:
                max_ord_letter = ord_letter
            
        if cnt > max_cnt:
            
            max_cnt = cnt
            max_ord_letter = ord_letter
    
    return chr(max_ord_letter)


if __name__ == '__main__':
    

    print(checkio('ZZZCCCAAA'))


