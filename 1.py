user_input=input(" ")

if user_input==" ":
    user_input=None
    print("no input provided")
else:
    print("entered value: {user_input}, Type: {type(user_input)}")