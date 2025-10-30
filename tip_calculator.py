total = float(input("Enter the total amount of the bill: $"))
party_num = int(input("How many people are in the party?: "))

tip_percentage = float(input("What percentage tip would you like to leave? %"))

total_after_tip = (total + (1.00 * tip_percentage))
print(f"The total bill with tip is: ${total_after_tip}")

total_each = total_after_tip / party_num
print(f"Each person in the party will pay ${round(total_each, 2)}")