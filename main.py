print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")

total = 1000
for i in range(10):
   total += (total * 0.05)

   total1 = str(round(total, 2))
   print("Year", i+1, "is", total1)
answer = total - 1000
answer = str(round(answer, 2))
print("You paid", answer, "in interest!")
