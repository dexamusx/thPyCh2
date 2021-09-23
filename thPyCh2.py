import math
#Exercise 1
#Repeating my advice from the previous chapter, whenever you learn a new feature,
#you should try it out in interactive mode and make errors on purpose to see what goes wrong.
#We’ve seen that n = 42 is legal. What about 42 = n? How about x = y = 1?
#In some languages every statement ends with a semi-colon, ;.
#What happens if you put a semi-colon at the end of a Python statement?
#What if you put a period at the end of a statement?
#In math notation you can multiply x and y like this: x y.
#What happens if you try that in Python?

n = 42;

#42 = n;
#^ gives a syntax error, cannot assign to literal value

x = y = 1;
#this works, sets both x and y to 1

print("I already end every line with a semicolon out of habit because of experience with other languages.");
#and it looks nicer to me
#so ending with a semicolon doesnt change anything

#print("you cant end a line of code with a period").
#its invalid syntax and gives that error

#z = x y
#the line above gives a syntax error, you would need to use a *

x = 3;
y = 5;
z = x * y;
print("x = "+str(x));
print("y = "+str(y));
print("z = x * y");
print(str(z)+" = "+str(x)+" * "+str(y));

#Exercise 2
#Practice using the Python interpreter as a calculator: The volume of a sphere with radius r is 4/3 π r3.
#What is the volume of a sphere with radius 5?
def sphere_volume(n):
    sphereRad = n;
    sphereVol = (sphereRad * 4/3) * (math.pi) * (sphereRad ** 3);
    #print(sphereRad ** 3);
    print("the volume of a sphere with radius "+str(sphereRad)+" would be "+str(sphereVol));

sphere_volume(5);
sphere_input = input("radius of the sphere? ");
sphere_volume(int(sphere_input));

#Suppose the cover price of a book is 24.95 but bookstores get a 40 percent discount.
#Shipping costs $3 for the first copy and 75 cents for each additional copy.
#What is the total wholesale cost for 60 copies?
book_retail = 24.95;
store_price = book_retail * .6;
#print(store_price);
#it returns store_price as 14.96999999999999 instead of 14.97, do you know why?
#it makes my answer 1 cent off which isnt much but it bothers me that I dont know whats causing it
book_count = 60;
shipping_price = 3 + (.75 * (book_count - 1));
total_wholesale = ((store_price * book_count) + shipping_price);
total_wholesale_dollars = int(total_wholesale // 1);
#print(total_wholesale - total_wholesale_dollars);
#print(total_wholesale);
#print(total_wholesale_dollars);
total_wholesale_cents = int(((total_wholesale - total_wholesale_dollars) // .01));
#print(total_wholesale_cents);
print("It would cost the store $"+str(total_wholesale_dollars)+"."+str(total_wholesale_cents)+" for all of the books.");
#should be one cent higher but it cuts off the .99999999, see line 57

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
#then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
easy_pace = 8 * 60 + 15;
#print(easy_pace);
fast_pace = 7 * 60 + 12;
time_start = 6 * 60 * 60 + 52 * 60;
#print(time_start);
time_end = time_start + easy_pace * 2 + fast_pace * 3;
#print("time end is"+str(time_end));
time_end_hour = time_end//(60*60);
time_end_min = ((time_end - time_end_hour * 60 * 60) // 60);
time_end_sec = (time_end - (time_end_hour * 60 * 60) - (time_end_min * 60));
if(time_end_sec < 10):
    time_print_sec = str("0"+str(time_end_sec));
else:
    time_print_sec = str(time_end_sec);
if(time_end_min < 10):
    time_print_min = str("0"+str(time_end_min));
else:
    time_print_min = str(time_end_min);
#print(time_end_sec);
print("you would get home at "+str(time_end_hour)+":"+time_print_min+":"+time_print_sec);
