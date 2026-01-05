def reverse(str):
    rev = ""

    for ch in str:
        rev = ch + rev 

    return rev 

def charFreq(str):
    freq = {}

    for ch in str:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    return freq

def vowel_consonant_count(str):
    vowels = "aeiou"

    v = c = 0
    for ch in str.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1 
            else:
                c += 1
    
    return v, c
    
def first_non_repeating(str):
    freq = {}

    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str:
        if freq[ch] == 1:
            return ch
    
    return None
        
def removeDuplicates(str):
    result = ""
    seen = set()

    for ch in str:
        if ch not in seen:
            seen.add(ch)
            result += ch
    
    return result


print("Reverse String: ", reverse("hello"))
print("Character Freq Map", charFreq("aaaaaaabbbbbbbccccdddd"))
vowels, consonants = vowel_consonant_count("aaaaaaabbbbbbbccccdddd")
print(f"Vowels: {vowels}, Consonants: {consonants}")
print(first_non_repeating("aaaaaabccccd"))
print(removeDuplicates("aaaaaabccccd"))