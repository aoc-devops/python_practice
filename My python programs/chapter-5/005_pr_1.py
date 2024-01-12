# program to create dictionary of hindi words to their meaning in english and allow user to see it by input 
dict={"pankha":"fan",
"pan":"leaf",
"tambakhu":"tobaco",
"pani":"water"}

a=input("enter hindi word\n")
print(dict[a])
print(dict.get(a))