# Word counter

def count_words_in_sentence(sentence):
    words = sentence.split()
    num_words = len(words)
    return num_words

sentence = input("Put your sentence: ")
print(f"The sentence '{sentence}' has {count_words_in_sentence(sentence)} words.")

