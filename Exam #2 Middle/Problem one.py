journey_cost = float(input())
number_of_months = int(input())

save_money = 0

for every_month in range(number_of_months):
    if every_month % 3 == 0:
        save_money -= save_money * 0.16
    if every_month % 4 == 0:
        save_money += save_money * 0.25
    save_money += journey_cost * 0.25

if save_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {(save_money - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_cost - save_money):.2f}lv. more.")
