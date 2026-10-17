"""Lesson 1.6: Clean a messy user question and build an AI prompt."""

name = input("Your name: ")
question = input("Your question: ")

# Why: Cleaning user input removes unwanted spaces and makes names consistent.
clean_name = name.strip().title()

# Why: Clean questions are easier to read and prepare for an AI model.
clean_question = question.strip().capitalize()

# Replace a bad word before sending the question to the AI model.
clean_question = clean_question.replace("stupid", "***")

character_count = len(clean_question)
estimated_tokens = round(character_count / 4)

mentions_python = "python" in clean_question.lower()

short_question = clean_question[:150]

prompt = f"""You are a helpful Python tutor.
Hello {clean_name}!
Answer the following question clearly and simply.
Question: {short_question}"""

print("=" * 40)
print(f"Name: {clean_name}")
print(f"Question: {clean_question}")
print(f"Characters: {character_count}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print("AI Prompt:")
print(prompt)
print("=" * 40)

# Practice price: 0.50 PKR per 1,000 tokens.
price_per_1k_tokens = 0.50
estimated_cost = estimated_tokens / 1000 * price_per_1k_tokens

print(f"Estimated cost: {estimated_cost:.2f} PKR")
