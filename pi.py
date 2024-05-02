text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

cleaned_text = ''.join(c for c in text if c not in ',.')

word_lengths = list(map(len, cleaned_text.split()))

result = ''.join(map(str, word_lengths))

print(result)
