
# Function to calculate final amount
def calculate_final_amount():
    # Step 1: Get the purchase amount from the user
    purchase_amount = float(input("Enter the purchase amount: $"))

    # Step 2: Apply the discount based on the purchase amount
    if purchase_amount < 100:
        discount = 0
    elif 100 <= purchase_amount <= 500:
        discount = 0.10  # 10% discount
    else:
        discount = 0.20  # 20% discount
    
    discounted_amount = purchase_amount * (1 - discount)
    
    # Step 3: Calculate the tax based on the discounted amount
    if discounted_amount < 200:
        tax = 0.05  # 5% tax
    else:
        tax = 0.08  # 8% tax
    
    tax_amount = discounted_amount * tax
    
    # Step 4: Calculate the final amount to pay
    final_amount = discounted_amount + tax_amount
    
    # Step 5: Display the results
    print(f"\n--- Summary ---")
    print(f"Original Purchase Amount: ${purchase_amount:.2f}")
    print(f"Discount Applied: ${purchase_amount * discount:.2f}")
    print(f"Tax Applied: ${tax_amount:.2f}")
    print(f"Final Amount to Pay: ${final_amount:.2f}")

# Call the function to run the program
calculate_final_amount()