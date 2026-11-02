# Ask for a sentence and clean it using strip().
Sentences = (input("Enter your sentence: ")).strip()
Words = Sentences.strip()
# Count characters and words.
print("Characters: ", len(Words))
print("Words: ", len(Words.split()))
# Ask for a word and find its first index.
Word = (input("Enter a word to find: "))
print("Found at index: ", Words.find(Word))
# Ask for a replacement word.
Replacement = (input("Enter a word to replace: "))
new_sentence = Sentences.replace(Word, Replacement)
print("Replaced: ", (new_sentence))
# Print the final sentence in uppercase.
print("Uppercase: ", new_sentence.upper())
