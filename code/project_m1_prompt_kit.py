"""Create ready-to-use AI prompts for a local business owner."""

business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
monthly_budget = int(input("Monthly budget (PKR): "))

# We collect the business details so the prompts are specific.
# The budget is converted to an integer because it is a number.
# F-strings let us insert the business details directly into each prompt.

print()
print("=========================================")
print(f"   AI Prompt Kit for {business_name}")
print("=========================================")

print()
print("[1] Marketing")
print(f"Write a short Instagram post for {business_name}, a {business_type} in {city}.")
print(f"Target {customers}. Use a friendly tone and include 1 call to action.")

print()
print("[2] Customer Service")
print(f"You are the manager of {business_name}.")
print("Write a polite reply to a customer whose order arrived late.")
print("Apologise and offer a small discount.")

print()
print("[3] Growth")
print(
    f"Suggest 3 low-cost AI tools a {business_type} in {city} "
    f"can use to attract {customers} with a budget of {monthly_budget} PKR per month."
)