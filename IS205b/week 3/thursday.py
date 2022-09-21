score = input("Enter score: ")
score = float(score)
# if score >= 0:
#     print("pass")
# elif score <= 1:
#     print("pass")
# else:
#     print("invalid score")

if (score <= 1) and (score >= 0):
    if score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    else:
        print("F")
else:
    print("invalid score")
