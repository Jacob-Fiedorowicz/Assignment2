# AI Review: Assignment 2

Ask an AI assistant to review one of your functions, or to suggest test cases for it.
Then fill in each section below. Replace every (write_here) with your own words.

## 1. The function and your prompt

Function I chose: cost_of_repeating_course

The exact prompt I used: Can you check my cost_of_repeating_course function to make sure that it gives the correct amount back of repeating a class when annual_cost and credits are given to it?

(Not needed, but I want it in here) The exact answer AI gave:
"The original function wasn’t calculating the cost of a 3-credit course: it multiplied the per-credit cost by the number of semesters in a year. I updated it to multiply by CS1430_CREDITS instead.

With an annual cost of $24,000 and 12 credits, the cost per credit is $1,000, so repeating a 3-credit course would cost $3,000 for one semester. I didn’t run the tests."

## 2. One suggestion I accepted

What the AI suggested: It suggested that I remove SEMESTERS_PER_YEAR and replace it with CS1430_CREDITS

My evidence that it was right (a check.py result, a calculation by hand, or a test I ran):
I did the math in my head, and its resoning was right. I was multiplying my cost_per_credit by two, for two semesters. This was wrong, and AI pointed it out, since I was only multiplying one credit by 2, instead of getting all 3 credits that CS1430 was worth. I was only doubling one credit, not 3

## 3. One suggestion I rejected or changed

What the AI suggested: It suggested to replace SEMESTER_PER_YEAR and replace it with CS1430_CREDITS

Why I rejected or changed it, and what I did instead:
I rejected the change, since I still needed that in there. Since it was supposed to be for a second time, meaning it was double credits, I had to have SEMESTER_PER_YEAR in their, so that it would multiply by 2 years. It told me to completely remove it and replace it with just one year of credits, which I rejected.
