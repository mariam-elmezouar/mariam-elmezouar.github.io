
%% Exercise 1: Cigar party

numberCigars = input("How many cigars are you planning on bringing? ");
dayOfTheWeek = input("Remind me, what day is it? ",'s');

if (numberCigars <= 60 && numberCigars >= 40) && (dayOfTheWeek ~= "Sunday" && dayOfTheWeek ~= "Saturday")
    disp("Party On")
elseif (dayOfTheWeek == "Sunday" || dayOfTheWeek == "Saturday") && numberCigars >= 40
    disp("Party On")
else
    disp("Lame")
end
    

%% Exercise 2: Number 6

a = input("Give me a number: ");
b = input("Give me another number: ");

if (a == 6 | b == 6) | (a+b ==6) | (a-b == 6) | (b-a == 6)
    disp("True")

end

%% Exercise 3: Course planning

CSE101 = input("Have you taken CSE101? Answer by 1 for Yes and by 0 for No ---- ");
MAE101 = input("Have you taken MAE101? Answer by 1 for Yes and by 0 for No ---- ");
EEE243 = input("Have you taken EEE243? Answer by 1 for Yes and by 0 for No ---- ");

if CSE101 & MAE101 & ~EEE243
    disp("Time to enroll in EEE243 and learn some programming in C.")
end

%% Exercise 4: Letter grade

grade = input("What's your assignment grade? ");

if grade >= 80 & grade <= 100
    disp("A")
elseif grade >= 65 & grade <= 79.999
    disp("B")
elseif grade >= 50 & grade <= 64.999
    disp("C")
elseif grade < 50
    disp("F")
else
    disp("Invalid grade")
end

%% Exercise 5: Number generator

for x = 21:1:50
    disp(x)
end

%% Exercise 6: Number generator 2

for x = 5:5:100
    disp(x)
end

%% Exercise 7: Divisors

number = input("Enter an integer and I will tell you all its divisors: ");
flag = 0;

for x = 2:number-1
    if mod(number,x) == 0
        disp(x + " is a divisor")
        flag = 1;
    end
end

if flag == 0
    disp(number + " is prime")
end

%% Exercise 8: Draw triangle

size = input("Enter the size of the trianle base: ");

for x = 1:size
    currentRow = "";
    for y = 1:x
        currentRow = currentRow + "* ";
    end
    disp(currentRow)
end

% or

for x = 1:size
    for y = 1:x
        fprintf("* ")
    end
    fprintf("\n")
end



