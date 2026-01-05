def checkPalindrome(s):
    chars = list(s)

    i, j = 0, len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            print("String is NOT a palindrome")
            return
        i += 1
        j -= 1

    print("String IS a palindrome")


def checkAnagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    return sorted(s1) == sorted(s2)


print("\nPALINDROME CHECK\n")
text = input("Enter a String: ").lower()
checkPalindrome(text)


print("\nANAGRAM CHECK\n")
word1 = input("Word 1: ").lower()
word2 = input("Word 2: ").lower()

if checkAnagram(word1, word2):
    print("Strings ARE anagrams")
else:
    print("Strings are NOT anagrams")
