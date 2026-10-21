"""
AI Front Desk for Sweet Crumbs bakery.

This tool answers common bakery questions, calculates price quotes,
and prepares AI-ready prompts for questions that the rules cannot answer.
"""

BOT_NAME = "Sweet Crumbs Desk"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K = 0.10

print("=" * 50)
print("   Sweet Crumbs Desk: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()

messages = 0
answered_by_rules = 0
unanswered = 0
number_of_quotes = 0
total_quoted_value = 0
total_ai_cost = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()

    if message == "":
        print(f"{BOT_NAME}: Please enter a question.")
        continue

    messages += 1

    # Complaint comes first so unhappy customers reach a human immediately.
    if "refund" in message or "complaint" in message or "late" in message:
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")
        answered_by_rules += 1

    # Exact greeting checks avoid treating words such as "which" as greetings.
    elif (
        message == "hi"
        or message == "hello"
        or message == "hey"
        or message.startswith("hi ")
        or message.startswith("hello ")
        or message.startswith("hey ")
        or message.startswith("good morning")
    ):
        print(f"{BOT_NAME}: Hello! How can I help you today?")
        answered_by_rules += 1

    elif message == "bye" or message.startswith("bye "):
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    elif "hours" in message or "open" in message or "timing" in message:
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")
        answered_by_rules += 1

    elif "location" in message or "where" in message or "address" in message:
        print(f"{BOT_NAME}: We are located in Lahore.")
        answered_by_rules += 1

    elif "delivery" in message or "deliver" in message:
        print(f"{BOT_NAME}: Delivery is available for {DELIVERY_FEE:,} PKR.")
        answered_by_rules += 1

    elif "fee" in message or "fees" in message or "charge" in message:
        print(f"{BOT_NAME}: Our standard delivery fee is {DELIVERY_FEE:,} PKR.")
        answered_by_rules += 1

    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        quantity_text = input(f"{BOT_NAME}: How many? ").strip()

        # Checking digits prevents a simple quantity mistake from crashing the program.
        if not quantity_text.isdigit():
            print(f"{BOT_NAME}: Please enter the quantity using numbers only.")
            continue

        quantity = int(quantity_text)

        if item == "cupcake":
            price = 250
        elif item == "brownie":
            price = 300
        elif item == "chocolate cake":
            price = 1500
        else:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
            continue

        subtotal = price * quantity

        # The discount is calculated before delivery so the free-delivery
        # decision is based on the discounted order value.
        if quantity >= 10:
            discount = subtotal * 0.10
        else:
            discount = 0

        discounted_total = subtotal - discount

        if discounted_total >= FREE_DELIVERY_LIMIT:
            delivery = 0
        else:
            delivery = DELIVERY_FEE

        total = discounted_total + delivery

        print(
            f"{BOT_NAME}: {quantity} x {item} = {subtotal:,.0f} PKR"
        )
        print(
            f"     Discount: -{discount:,.0f} PKR | "
            f"Delivery: {delivery:,.0f} PKR"
        )
        print(f"     Total: {total:,.0f} PKR")

        number_of_quotes += 1
        total_quoted_value += total
        answered_by_rules += 1

    else:
        cleaned_question = message.capitalize()[:150]
        estimated_tokens = round(len(cleaned_question) / 4)

        if (
            "phone" in message
            or "cnic" in message
            or "address" in message
        ):
            selected_model = "llama3.2 (local, private)"
            estimated_cost = 0

            print(
                f"{BOT_NAME}: Good question! Routed to: "
                f"{selected_model} (~{estimated_tokens} tokens)"
            )

            print(
                f"""     Prompt: You are the assistant of Sweet Crumbs bakery.
     Answer {customer_name} in 2 short lines. Question: {cleaned_question}"""
            )

        else:
            selected_model = "small cloud model (cheap)"
            estimated_cost = (estimated_tokens / 1000) * CLOUD_PRICE_PER_1K

            print(
                f"{BOT_NAME}: Good question! Routed to: "
                f"{selected_model} (~{estimated_tokens} tokens)"
            )

            print(
                f"""     Prompt: You are the assistant of Sweet Crumbs bakery.
     Answer {customer_name} in 2 short lines. Question: {cleaned_question}"""
            )

        unanswered += 1
        total_ai_cost += estimated_cost

print("=" * 50)
print("Session report")
print(
    f"Messages: {messages} | "
    f"Answered by rules: {answered_by_rules} | "
    f"Unanswered: {unanswered}"
)
print(
    f"Quotes: {number_of_quotes} | "
    f"Quoted value: {total_quoted_value:,.0f} PKR"
)
print(
    f"Estimated AI cost for unanswered questions: "
    f"{total_ai_cost:.4f} PKR"
)
print("=" * 50)