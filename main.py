#TIP CALCULATOR
#food amount = 100
#tip amount = 20% tip
food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter tip percentage: ')) / 100
tip_amount = food_amount * tip_percentage
print(tip_amount)
total = food_amount + tip_amount
print('$' + str(total))
