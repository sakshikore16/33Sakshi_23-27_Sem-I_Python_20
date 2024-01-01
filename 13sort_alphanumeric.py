# 13. WAP to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically.

text = input("Enter a sentence: ")
words = text.lower().split()

word_freq = {}
for word in words:
    word = word.strip(".,!?")
    word_freq[word] = word_freq.get(word, 0) + 1

sorted_keys = sorted(word_freq)

print("Word frequencies (sorted alphanumerically):")
for key in sorted_keys:
    print(f"{key}: {word_freq[key]}")
