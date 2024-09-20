# Strings (str): Sequences of characters, such as "Hello, world!".
text = "recommended"
text_two = "two"  # ''
text_three = """three
test"""
text_four = "text for"
text_five = "text five"
print(text, text_two, text_three, text_four, text_five)
# Escape characters
print("text \n six")  # Wrap outline
print("text ' seven'")  # ignore a characters
print("text \\ eight")  # show a \
# Know a string length
test_name = "Daniel"
print(len(test_name))  # print the number of characters on this string
# dynamic print
print(f"{text_five},{text_four},{text_three}")
# some features of strings
features_test = "featutes test"
print(features_test.upper())
print(features_test.lower())
print(features_test.strip())
print(features_test.lstrip())
print(features_test.rstrip())
print(features_test.find("st"))
print("https://www.pexels.com/search/ocean/".replace("ocean", "sea"))
# Slice; manipulating parts of a string, through indexes
word = "my test word"
print(word[6])
print(word[0])  # return the first character
print(word[-1])  # return the final character
print(word.index("d"))  # search using a index character, and return the sames
print(word[word.index("3")], [word[7]])  # dynamic mode with multiples results
# it will never print the number defined as final, but rather the number before it.
# In case of non ": final definition" the same will interact until the end
print(word[0:-1])  # the : define the final of the operation
print(word[3:])
print(
    word[:-5]
)  # sets the index target to take out, before starting as soon as it finishes advancing
# This way, we can know when was the last time that such character was defined in the string.
print(word.rindex("o"))
# Sprit e join
# The separation of items in a list is done by spaces.
# However, it is possible to separate by a special character and define from where to what point to separate.
full_name = "Gabriel, De, Lucca"
print(full_name.split())  # Using the stand parameter the spaces
print(full_name.split(","))  # using a special character
print(full_name.split(",", "2"))  # special character with limit of iteration
# combining string and parts of string and separating with special characters
my_prhase = "the dogs barks"
print(",".join(my_prhase))
print("".join(my_prhase))
