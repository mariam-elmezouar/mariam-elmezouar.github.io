USE StudentDB;

/**************************************************************
  1- Retrieve IDs and names of students with a GPA greater than 
  3.5.
**************************************************************/



/**************************************************************
  2- Retrieve names and GPAs of students from high schools with less than 1000 students who are 
  applying for Computer Science at Berkeley.
**************************************************************/


/**************************************************************
 3- Retrieve distinct locations and ranks of campuses with enrollments over 30,000 that have applicants to Computer Science programs, eliminating duplicate entries.
**************************************************************/







/**************************************************************
 4- Retrieve application information sorted first by campus rank in ascending order and then by student GPA in descending order.
**************************************************************/





/**************************************************************
  5- Retrieve names of students applying to any bio-related majors including biology, bioengineering, or marine biology.
**************************************************************/





/**************************************************************
   6- Create a view to calculate and display a scaled GPA for students, scaling it based on the size of their high school divided by 1000, and then drop the view after selection.
**************************************************************/







/**************************************************************
  7- Identify pairs of students who share the same GPA but have different IDs.
**************************************************************/








/**************************************************************
 8- Combine names from the student table with majors from the apply table into a single list without duplicates.
**************************************************************/





/**************************************************************
 9- Identify IDs of students who have applied to both Computer Science (CS) and Electrical Engineering (EE).
**************************************************************/




/**************************************************************
 10- Identify IDs of students who applied to CS but not EE 
**************************************************************/





/**************************************************************  
 11- Identify IDs and names of students applying to CS. Use a subquery with IN
**************************************************************/











/**************************************************************
12-  Idnetify IDs and names of students who applied to CS but not EE. Use a SUBQUERY WITH NOT IN
**************************************************************/







/**************************************************************
 13- Find students who have at least one other student with the same GPA and high school size (SUBQUERY WITH EXISTS).
**************************************************************/





/**************************************************************
 14- BASIC AGGREGATION (AVG)
  Average GPA of all students
**************************************************************/




/**************************************************************
 15- AGGREGATION OVER JOIN
  Average GPA of students applying to CS
**************************************************************/



/**************************************************************
 16- BASIC AGGREGATION (COUNT)
  Number of campuses bigger than 30,000
**************************************************************/






/**************************************************************
 17- GROUP BY
  Number of applications to each campus
**************************************************************/







/**************************************************************
 18- MULTIPLE AGGREGATIONS
 Find the minimum and maximum applicant GPA for each campus and major.
**************************************************************/







/**************************************************************
  19- UPDATE
  Accept applicants to Los Angeles with GPA > 3.6 and turn
  them into urban-studies majors
**************************************************************/

