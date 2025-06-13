sentence = "   Hello,     World!   A    lot   of    spaces.   "
print(sentence)

words = sentence.split()
print(words)

new_sentence = " ".join(words)
print(new_sentence)
