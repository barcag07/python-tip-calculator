total = float(input("Enter the total amount of the bill: $"))
party_num = int(input("How many people are in the party?: "))

# Add a new stage that will ask how much the user wants to tip

total_each = (total * 1.15) / party_num

print(f"Each person in the party will pay ${round(total_each, 2)}")