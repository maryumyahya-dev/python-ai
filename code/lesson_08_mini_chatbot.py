"""Lesson 1.8: Rule-based business helper chatbot for Sweet Crumbs Bakery."""

BOT = "Sweet Crumbs Bot"

print(
    f"{BOT}: Hi! I can help with hours, prices, location, orders and complaints."
)
print(f"{BOT}: Type 'bye' to exit.")

# Why: Asking for the name before the loop lets the bot remember the user.
name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"{BOT}: Nice to meet you, {name}!")

count = 0
unanswered = 0
complaints = 0

while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    # Why: Exit must be checked every time so the user can safely end the chat.
    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thanks for visiting.")
        break

    # Stretch: connect the customer to a human agent.
    elif "agent" in message or "human" in message:
        print(f"{BOT}: Connecting you to a human...")
        break

    elif message == "":
        print(f"{BOT}: Please type a question.")

    # Why: Complaints come first so unhappy customers reach a human quickly.
    elif (
        "refund" in message
        or "complaint" in message
        or "late" in message
    ):
        complaints += 1
        print(
            f"{BOT}: Sorry about that, {name}. "
            "A manager will contact you within 1 hour."
        )

    elif "hour" in message or "open" in message or "time" in message:
        print(f"{BOT}: We are open 9 am to 10 pm, every day.")

    elif (
        "price" in message
        or "cost" in message
        or "how much" in message
    ):
        print(
            f"{BOT}: Cakes start at 1,500 PKR. "
            "Cupcakes are 250 PKR each."
        )

    elif (
        "where" in message
        or "location" in message
        or "address" in message
    ):
        print(f"{BOT}: We are on Main Boulevard, Lahore.")

    elif "order" in message or "delivery" in message:
        print(
            f"{BOT}: You can order through WhatsApp. "
            "Delivery is free over 3,000 PKR."
        )

    elif (
        message == "hi"
        or message == "hello"
        or message.startswith("salam")
    ):
        print(f"{BOT}: Hello again, {name}! How can I help?")

    else:
        unanswered += 1

        prompt = (
            "You are the friendly assistant of Sweet Crumbs Bakery. "
            f"Answer in 2 short lines. Customer question: {message}"
        )

        print(
            f"{BOT}: I am not sure yet. "
            "In Module 2, an AI will answer using this prompt:"
        )
        print(f"  {prompt}")

print("=" * 40)
print(f"Chat summary: {count} messages")
print(f"Unanswered questions: {unanswered}")
print(f"Complaints received: {complaints}")
print("=" * 40)
