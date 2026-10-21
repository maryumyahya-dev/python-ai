# Module 1 Checkpoint 2 — AI Front Desk Design

## Business

**Business Name:** Sweet Crumbs  
**Business Type:** Bakery

The front desk answers common customer questions using free rules, calculates exact quotes, and prepares AI-ready prompts for questions that the rules cannot answer.

## Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | Sorry about that. A manager will call you within 1 hour. |
| Greeting | hi, hello, hey, good morning | Hello! How can I help you today? |
| Hours | hours, open, timing | We are open 9 am to 10 pm, every day. |
| Location | location, address, where | We are located in Lahore. |
| Delivery | delivery, deliver, delivery time | Delivery is available for 200 PKR. |
| Fees | fee, charge, charges | Standard delivery fee is 200 PKR. |

## Business Rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250 PKR, brownie 300 PKR, chocolate cake 1,500 PKR |
| Bulk discount | 10% off for 10 or more items |
| Delivery | 200 PKR, free from 3,000 PKR after discount |
| Private words | phone, cnic, address |
| Cloud model price | 0.10 PKR per 1,000 tokens |

## Rule Test Results

| You type | Expected | Pass? |
|---|---|---|
| WHAT are your hours | Hours reply; capitals and spaces handled |pass |
| which cake is best? | Fallback, not a greeting |pass |
| my order is late | Manager reply | pass|
| /quote, 1 of your most expensive item | Delivery fee charged | pass|
| /quote, a big order above the free-delivery limit | Delivery free |pass |
| /quote, 10 or more items | Discount applied |pass |
| /quote, an item not on your menu | Not on our menu, no crash |pass |
| A question with "phone" or "cnic" | Local model, cost 0 | pass|
| Press Enter with no text | Asks again |pass |
| BYE | Goodbye and session report | pass|