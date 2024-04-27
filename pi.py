text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
word_lengths = list(map(len, text.split()))

result = ''.join(map(str, word_lengths))

print(result)
