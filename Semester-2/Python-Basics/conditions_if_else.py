# -------------------------------------------------------------------
# Taking a letter as input and checking if it is vowel or consonant
# -------------------------------------------------------------------

c = input("Enter a letter: ")

if c.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# -------------------------------------------------------------------
# GRADING SYSTEM
# -------------------------------------------------------------------
# Taking marks as input and giving grade based as
# A if equal to or greater than 90
# B if equal to or greater than 75
# C if equal to or greater than 60
# D if equal to or greater than 45
# E if greater than 33
# Fail equal to if less than 33 
# -------------------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks > 100 or marks<0:
    print("Invalid marks entered.")
elif marks >= 90 :
    print("Grade: A") 
elif marks >= 75:
    print("Grade: B") 
elif marks >= 60:
    print("Grade: C") 
elif marks >= 45:
    print("Grade: D") 
elif marks > 33:
    print("Grade: E") 
else:
    print("Fail") 

# -------------------------------------------------------------------