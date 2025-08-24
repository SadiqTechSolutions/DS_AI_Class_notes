# Checkout Calculator
# This program calculates the total cost of items with a potential discount

# 1. Define variables for the prices of three items
item1_price = 10.50  # Price of first item (float)
item2_price = 20.00  # Price of second item (float)
item3_price = 5.25   # Price of third item (float)

# 2. Calculate the subtotal of all items
subtotal = item1_price*2 + item2_price*4 + item3_price*3

# 3. Define a boolean variable for membership status
has_membership = True  # Customer has a membership card

# 4. Determine eligibility for discount based on rules:
#    - Subtotal must be $30.00 or more AND
#    - Customer must have a membership card
is_eligible_for_discount = (subtotal >= 30.00) and has_membership

# 5. Calculate the final total

if is_eligible_for_discount:
    final_total = subtotal * 0.9  # Apply 10% discount

final_total = subtotal

# 6. Print all results in a user-friendly receipt format
print("===== RECEIPT =====\n")

# Print individual item prices
print(f"Item 1: ${item1_price:.2f}")
print(f"Item 2: ${item2_price:.2f}")
print(f"Item 3: ${item3_price:.2f}")
print("-" * 20)

# Print subtotal
print(f"Subtotal: ${subtotal:.2f}")

# Print discount information
print(f"Membership: {has_membership}")
print(f"Discount Applied: {is_eligible_for_discount}")

# Print the final total
print("-" * 20)
print(f"Final Total: ${final_total:.2f}")
print("Thank you for shopping with us!")
print("====================")