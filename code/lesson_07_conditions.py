"""Lesson 1.7: Smart Model Router using conditions and operators."""

# Ask what kind of task the user wants the AI to handle.
task = input("Task (code / private / chat): ").strip().lower()

# input() returns text, so convert tokens to int before doing maths.
tokens = int(input("Estimated tokens: "))

# Ask whether the user is a paid user for the stretch requirement.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

# Why: Private data should stay on the user's laptop for better privacy.
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k = 0.0

# Why: Code tasks usually need a stronger model than simple chat tasks.
elif task == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k = 0.50

else:
    model = "small cloud model (cheap for chat)"
    price_per_1k = 0.20

# Calculate the estimated cost.
cost = tokens / 1000 * price_per_1k

# Warn the user when the request is longer than 4000 tokens.
if tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

# Stretch: free users with long requests should be encouraged to upgrade.
if paid_user == "no" and tokens > 2000:
    upgrade_message = "Upgrade to send long requests."
else:
    upgrade_message = ""

print("=" * 40)
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")
print(warning)

if upgrade_message:
    print(upgrade_message)

print("=" * 40)