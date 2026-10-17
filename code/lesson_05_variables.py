"""Lesson 1.5: AI Model Profile Card."""

model_name = "gemma3"
context_window = 128000
price_per_1k_tokens = 0.5
runs_locally = True

# Why: Clear variable names make AI configuration easy to understand.
print(f"Model name: {model_name} | Type: {type(model_name)}")

# Why: type() helps us check that each configuration value has the correct type.
print(f"Context window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} | Type: {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} | Type: {type(runs_locally)}")

tokens_used = int(input("How many tokens does one chat use? "))

cost = tokens_used / 1000 * price_per_1k_tokens

print(f"Estimated cost for one chat: {round(cost, 2)} PKR")

chats_per_day = int(input("How many chats per day? "))

monthly_cost = cost * chats_per_day * 30

print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")