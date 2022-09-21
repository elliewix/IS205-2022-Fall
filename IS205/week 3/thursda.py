#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("Enter score: ")
score = float(score)
# if score >= 0:
#     print("pass")
# elif score <= 1:
#     print("pass")
if (score >= 0) and (score <= 1):
    if score >= .9:
        print("A")
    elif score >=.8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    else:
        print("F")
else:
    print("score out of bounds")

# print letter grade at the end

