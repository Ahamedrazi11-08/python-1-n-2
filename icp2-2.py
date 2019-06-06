#definition of function string_alternative
def string_alternative(actualstring):
    newstr = actualstring[::2];
    print("printing alternative characters of actual string")
    print(newstr);

#calling function string_alternative
print("calling function string_alternative");
string_alternative("Good evening")