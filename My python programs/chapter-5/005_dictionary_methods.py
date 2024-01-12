laladict={"mobile":"cell phone","dog":"animal","cheeta":"fastest animal",9096119622:1122,"marks":[10, 90, 25],
"laladict1":{"elephant":"big animal"}}

print(laladict.keys()) # printing all keys mentioned in dictionry
print(laladict.values()) #  printing all values mentioned in dictionry
# print(laladict.items()) # Prints the (key, value) for all contents of the dictionary 
laladict.update({"cat":"tiger family"}) # updating new key value pair in dictionary
print(laladict)

# adding multiple key value pairs
laladict1={"farary":"fastest car", "pagani":"hypercar", "nexon":"5star"}
laladict.update(laladict1)
print(laladict)

# print(laladict.get("dog")) # Prints value associated with key "dog"
# print(laladict["dog"]) # Prints value associated with key "dog"

# # The difference between .get and [] sytax in Dictionaries?
# print(laladict.get("dog2")) # Returns None as dog2 is not present in the dictionary
# print(laladict["dog2"]) # throws an error as dog2 is not present in the dictionary
