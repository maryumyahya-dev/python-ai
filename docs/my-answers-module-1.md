# Module 1 Quick Checks

## Lesson 1.1
1.1: Q1 b, Q2 c, Q3 b, Q4 c, Q5 b, Q6 Hello from kimi!

## Lesson 1.2
1.2: Q1 c, Q2 b, Q3 b, Q4 b, Q5 b, Q6 Python 3.13.16

## Lesson 1.3
1.3: Q1 b, Q2 c, Q3 b, Q4 b, Q5 b, Q6 Hi, I am Ali and I will become an AI Agent Developer.

## Lesson 1.4
1.4: Q1 c, Q2 b, Q3 c, Q4 b, Q5 c, Q6 201

## Lesson 1.5

1. What does int(3.9) return?
   Answer: 3. It cuts off the decimal part and does not round.

2. Why does price = input("Price: ") followed by price * 2 not double the number?
   Answer: Because input() always returns text (str). We must convert it to a number using int() or float() before doing maths.

3. Is 2nd_model a valid variable name? Fix it.
   Answer: No. A variable name cannot start with a number. A correct name is model_2.

   ## Lesson 1.6

1. What does "Python for AI"[-2:] return?
   Answer: "AI"

2. Why does "Refund" in "i want a refund" give False, and how do you fix it?
   Answer: Because Python is case-sensitive. "Refund" has a capital R, while the text has lowercase "refund". We can fix it by using "refund" in text.lower().

3. After name = " ali " and name.strip(), why does print(len(name)) still show 5?
   Answer: Because strings are immutable and strip() returns a new string. We must save the result with name = name.strip().