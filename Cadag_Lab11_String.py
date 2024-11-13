word_count = 0
words = []
matched_words = []

while word_count < 10:
    word = input("Enter a word: ")
    words.append(word)
    word_count += 1

num = int(input("Enter the minimum number of letters to display words with that many or more letters: "))

for i in words:
    if len(i) >= num: 
        matched_words.append(i)

print("Words with at least", num, "letters:", matched_words)
