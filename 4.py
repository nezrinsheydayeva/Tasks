sn=7
for attempt in range(3):
    guess=int(input())

    if guess<sn:
        print("low")
    elif guess>sn:
        print("high")
    else:
        print("congraatulations")
        break
else:
    print("sorry")