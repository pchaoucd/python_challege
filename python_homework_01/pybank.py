import csv

month_total= 0
profit_loss= 0
greatest_increase_amount = 0
greatest_increase_date = None
greatest_decrease_amount = 0
greatest_decrease_date = None

with open ("budget_data.csv","r") as csvfile:
    reader= csv.reader(csvfile)

    previous_month_amount = None
    for row in reader:
        if row[1]=="Profit/Losses":
            continue

        month_total+=1
        profit_loss = profit_loss + int(row[1])

        current_month_amount = int(row[1])
        current_month = row[0]

        if previous_month_amount is None:
            previous_month_amount = current_month_amount

        delta = current_month_amount - previous_month_amount
        if delta > greatest_increase_amount:
            greatest_increase_amount = delta
            greatest_increase_date = current_month
        if delta < greatest_decrease_amount:
            greatest_decrease_amount = delta
            greatest_decrease_date = current_month

        previous_month_amount = current_month_amount

#print(str(month_total))
#print(str(profit_loss))
#print(str(greatest_increase_amount))
#print(str(greatest_decrease_amount))

print("Financial Analysis")
print("----------------------------")     
print("Total month:"+str(month_total))
print("Total:$"+str(profit_loss))
print("Greatest Increase in Profits:"+ greatest_increase_date+ "("+"$"+ str(greatest_increase_amount)+")")
print("Greatest Decrease in Profits:"+ greatest_decrease_date+ "("+"$"+ str(greatest_decrease_amount)+")")

