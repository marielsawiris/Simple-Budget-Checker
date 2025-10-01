Item1 = 5
Item2 = 10
Item3 = 15

Total_Budget = 100
print("Total Budget:", Total_Budget)

Total_Cost = Item1 + Item2 + Item3
print("Total Cost:", Total_Cost)

Remaining_Budget = Total_Budget - Total_Cost
if Total_Cost <= Total_Budget:
    print("You are within your budget!")
    print("You will have", Remaining_Budget, "left over.")
else:
    print("You are over your budget.")
    print("You need an extra", abs(Remaining_Budget), "to buy these items.")