# fill the name and date in letter template
# letter= '''Dear <|NAME|>
# This mail is from Mart Research
# Congratulations you have selected for post of "Businesss Developement Ececutive"
# Date: <|DATE|>'''
# name=input("enter name")
# date=input("Enter date")
# letter=letter.replace("<|NAME|>", name)
# letter=letter.replace("<|DATE|>", date)
# print(letter)

# anothor method
letter= '''Dear name
This mail is from Mart Research
Congratulations you have selected for post of "Businesss Developement Ececutive"
Date: date'''
name=input("enter name")
date=input("Enter date")
letter=letter.replace("name", name)
letter=letter.replace("date", date)
print(letter)
