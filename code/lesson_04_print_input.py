"""Create an AI prompt from basic business information."""

name = input("Your name: ")

# We ask for the business type so the AI can give industry-specific suggestions.
business = input("Business type: ")

# We ask for the main problem so the generated solutions target a real business need.
problem = input("Biggest problem: ")

print(f"\nWelcome, {name}!")
print("--- Your AI Prompt ---")

prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(prompt)