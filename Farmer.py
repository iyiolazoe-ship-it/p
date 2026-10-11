field1=70
field2=200
field3=123
field4=172
field5=389

total= field1 + field2 + field3 + field4 + field5
average= total / 5

print("Total harvest :", total, "kg")
print("Average per field :", average, "kg")

# price per kg
price_per_kg = 15
earnings = total * price_per_kg
print("Earnings:", earnings, "kg")

bags = total // 25
leftover = total % 25

last_year=500
print("Better than last year? :",total > last_year )
print("Same as last year? :",total == last_year )
print("? :",total > last_year )

total +=30
print("After seed reserve :", total, "kg")

bags = total // 25
print("Final bag  packed :", total, "kj")