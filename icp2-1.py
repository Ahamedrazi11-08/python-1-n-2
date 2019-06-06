#creating empty list
l=[];
k =[];

#function to convert lbs to kgs
def lbstokgs(l):
    for element in l:
      kl = float(element) * 2.2;
      k.append(kl);
    print("weights of students in kilograms");
    print(k);

# reading number of students
length = int(input("enter the number of students"));

#reading weights in lbs and storing in list
for i in range(length):
    lbs = input("enter weights in lbs");
    l.append(lbs);

print("weights of students in lbs");
print(l);

#calling function which converts lbs to kgs
lbstokgs(l)







