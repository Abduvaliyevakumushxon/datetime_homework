#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime
s=datetime.date.today()
d=int(input('kiriting'))
l=s.year-d
print(l)