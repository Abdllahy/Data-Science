# a regular expression is a sequence of characters that maps to patterns or punctions

import re
# a regular expressions to find all matches of a pattern
# syntax: re.findall(regexpression(pattern), string)
# the regular expression is the pattern we are looking for in the string
movie_instances = re.findall(r"#movies", "I love watching action #movies. i really enjoyed watching The old guard.i can't wait to be back to the #movies again")
print(movie_instances)
print(type(movie_instances))
print("-----------------------")

# A regular expression that splits a string at each pattern match
# syntax: re.split(regexpression(pattern), string)
# the regular expression is the pattern we are looking for in the string
my_words = "Nice place to chill! i really enjoyed the music! I can't wait to be back again!"

print(re.split(r"!", my_words))
print("-----------------------")

# A regular expression that replaces one or many pattern matches with a string
# syntax: re.sub(regexpression(pattern), new/replacement, string)
my_Sentence = "I really like the blue and dark-blue color. I am thinking of getting  blue ducati."
print(re.sub(r"blue", "purple", my_Sentence))


