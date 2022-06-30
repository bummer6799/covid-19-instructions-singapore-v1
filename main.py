a = input("Did you receive a Health Risk Warning? (yes/no) \n")

yes = ("yes")
no = ("no")

if a == yes:
    print("Follow Protocol 3. 5 Days of monitoring. Test ART within 24 hours.")
elif a == no:
    b = input("Are you feeling well? (yes/no) \n")
    if b == yes:
        print("If you are worried, do ART Test.")
    elif b == no:
        print("Visit a doctor to assess on the next step.")
        quit()
    else:
        ()
else:()

c = input("What is the result of your ART test? (positive/negative) \n")

if c == ("Positive") or ("positive"):
    d = input("Are you feeling well? (yes/no) \n")
    if d == yes:
        e = int(input("What is your age?"))
        if 3 > e > 70:
            print("Request a Telemedicine consult to let the doctor advice.")
            quit()
        else:
            print("You should self-isolate for 72 hours at home.")
            quit()
    elif d == no:
        print("Request a Telemedicine consult to let the doctor advice.")
    else:
        ()
else:
    ()

if c == ("Negative") or ("negative"):
    print("You can leave your house for normal activity")
    quit()