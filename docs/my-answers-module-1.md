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

   ## Lesson 1.7

1. What do 17 // 5 and 17 % 5 return?
   Answer: 17 // 5 returns 3 because it is whole-number division. 17 % 5 returns 2 because it is the remainder.

2. Why is if task == "code" or "chat": always True? Write the fix.
   Answer: Because "chat" by itself is a non-empty string, so it is truthy. The correct condition is:
   if task == "code" or task == "chat":

3. score = 85. With if score > 50: above elif score > 80:, which message prints, and why?
   Answer: The message in the if block prints because 85 is greater than 50. Python runs the first True block and does not check the elif after that.

   ## Lesson 1.8

1. What does break do, and what happens without it in while True?
   Answer: break immediately stops the loop. Without break, while True keeps running forever until the program is stopped.

2. Why does "hi" in "which cake?" give True? How do you avoid it?
   Answer: Because the in operator checks whether "hi" appears anywhere inside the text. To avoid this, use an exact match such as message == "hi" or message == "hello".

3. Why must the complaint rule come before the order rule?
   Answer: Because a message like "my order is late" contains both "order" and "late". If the order rule comes first, it will answer with the order menu instead of sending the unhappy customer to a human.
   

   # Module 1 Quick Checks — Part 2

1.5: Q1 b, Q2 b, Q3 c, Q4 b, Q5 b, Q6 10.0

1.6: Q1 b, Q2 a, Q3 b, Q4 b, Q5 b, Q6 98765.4 PKR for 2,500,000 chats

1.7: Q1 b, Q2 b, Q3 b, Q4 b, Q5 a, Q6 Upgrade

1.8: Q1 b, Q2 b, Q3 d, Q4 a, Q5 b, Q6 3 messages, 1 unanswered