
# print("RobuComponents")
# print("==============================")

# customer = input("Enter Customer Name: ")
# product = input("Enter Product Name: ")
# quantity = int(input("Enter Quantity: "))
# price = float(input("Enter Price:"))
# discount_amount = float(input("Enter Discount Percentage: "))
# delivery = float(input("Enter Delivery Charge: "))
# total = price * quantity + delivery
# discount = total * discount_amount / 100
# final_bill = total - discount
# print("==============================")
# customer_email = input("Enter Customer Email: ")
# customer_address = input("Enter Customer Address: ")
# customer_phone = int(input("Enter Customer Phone Number: "))

# print("\n========== ORDER SUMMARY ==========")
# print("Customer Name:", customer)
# print("Product Name:", product)
# print("Price:", price)
# print("Quantity:", quantity)
# print("Delivery:", delivery)
# print("Discount:", discount_amount)
# print("Discount Amount:",(discount))
# print("-----------------------------------")
# print("Customer Email:", customer_email)
# print("Customer Address:", customer_address)
# print("Customer Phone:", customer_phone)
# print("\n")
# print("-----------------------------------")
# print("Final Bill:",(final_bill))
# print("===================================")

#------------------------task-3-------if /else-------------

# print("RobuComponents")
# print("======================")

# customer = input("Enter Customer Name: ")
# product = input("Enter Product Name: ")
# price = float(input("Enter Price: "))
# quantity = int(input("Enter Quantity: "))
# shipping = float(input("Enter Shipping Charge: "))
# total = price * quantity + shipping


# if price > 0 and quantity > 0 and total >= 500:
#     discount_percent = 10
# elif price > 0 and quantity > 0 and total >= 200:
#     discount_percent = 5
# elif price > 0 and quantity > 0:
#     discount_percent = 0
# else:
#     print("Invalid")

# discount = total * discount_percent / 100
# final_bill = total - discount

# print("\n========== ORDER SUMMARY ==========")
# print("Customer:", customer)
# print("Product:", product)
# print("Price:", price)
# print("Quantity:", quantity)
# print("Shipping:", shipping)
# print("Discount:", discount_percent)
# print("Discount Amount:",(discount))
# print("Final Bill:", (final_bill))


# ---------------calci--------------
# import numbers
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     answer = num1 + num2
# elif operator == "-":
#     answer = num1 - num2
# elif operator == "*":
#     answer = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         answer = num1 / num2
#     else:
#         answer = None
#         print("Cannot divide by zero!")

# if answer is not None:
#     print("Final Answer:", answer)


# ------------------------------------------------
Number=35

if Number > 95 and Number < 100:
    print("Grade A")
elif Number > 80 and Number < 95:
    print("Grade B")
elif Number > 70 and Number < 80:
    print("Grade C")
elif Number > 60 and Number < 70:
    print("Grade D")
else:
    print("Fail")