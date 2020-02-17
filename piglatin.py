"""
A module to translate English into Pig Latin.

Take consonants that start a word, place them at the end of the word and add
"ay".

If a word starts with a vowl, just append "ay" to the end of the word.
"""

VOWELS = ("a", "e", "i", "o", "u", )
PUNCTUATION = (".", "!", "?", ":", )
IGNORE = (",",  "-", "(", ")", "[", "]", "'", )


def translate(sentence):
    """
    Return an English sentence translated as Pig Latin.
    """
    result = []
    words = [word.lower() for word in sentence.split() if word.strip()]
    capitalize = True
    for word in words:
        if word[0] in VOWELS:
            head = word
            tail = "ay"
        else:
            head = word[1:]
            tail = word[0] + "ay"
        if capitalize:
            head = head.capitalize()
            capitalize = False
        if head[-1] in PUNCTUATION:
            tail += head[-1]
            head = head[:-1]
            capitalize = True
        elif head[-1] in IGNORE:
            tail += head[-1]
            head = head[:-1]
        result.append(head + tail)
    return ' '.join(result)
