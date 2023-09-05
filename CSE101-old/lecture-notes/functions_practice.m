disp("Grade calculator")

assignment1 = input("What was your grade on assignment 1? ");
assignment2 = input("What was your grade on assignment 2? ");
assignment3 = input("What was your grade on assignment 3? ");

x = calculateNumericGrade(assignment1, assignment2, assignment3);

letter_grade = convertToLetterGrade(x);

displayReport(letter_grade);

disp(displayReport(letter_grade)); % This is an error. Why?

function x = calculateNumericGrade(a, b, c)
	x = (a+b+c)/3;
end

function x = convertToLetterGrade(a)
	if a >= 50
        x = 'A';
    else
        x = 'B';
    end
end

function displayReport(a)
    if a == 'A'
        disp("Congrats. You got an " + a);
    else
        disp("Not bad. You got an " + a);
    end
end