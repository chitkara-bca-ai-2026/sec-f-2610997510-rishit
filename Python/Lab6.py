print("=" * 40)
print("       CLOTHING STORE BILLING SYSTEM")
print("=" * 40)

# 1. Accept customer's name
customer_name = input("Enter Customer Name: ")

# 2. Accept garment name
garment_name = input("Enter Garment Name: ")

# 3. Accept price of one garment
price = float(input("Enter Price of one Garment: "))

# 4. Accept number of garments
quantity = int(input("Enter Number of Garments: "))

# 5. Calculate total cost
total_amount = price * quantity

# 6. Display the bill
print("\n" + "=" * 40)
print("                 BILL")
print("=" * 40)

print("Customer Name :", customer_name)
print("Garment Name  :", garment_name)
print("Price per Unit: Rs.", price)
print("Quantity      :", quantity)
print("Total Amount  : Rs.", total_amount)

print("=" * 40)