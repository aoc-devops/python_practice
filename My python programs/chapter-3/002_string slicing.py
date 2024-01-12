name="Father"
print(name[0:2])
print(name[1:5])
print(name[-6:-1])
print(name[-5:-1]) # is same as name[1:5]
print(name[:6]) # is same as name[0:6]
print(name[0:]) # is same as name[0:6]

# Slicing with skip numbers
word="Fatherisgreat"
print(word[1:3:6])
print(word[1:4:7])