import csv
filename = "items.csv"

category_prices = {}

with open(filename, newline='') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        print("-----")
        print(row)



filename = "items.csv"

category_prices = {}

with open(filename, newline='') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        if len(row) == 16:
            # PARSE
            category = row[3]
            sell_price = row[5]
            currency = row[6]
            if currency == "bells" and sell_price.isnumeric():
                sell_value = int(sell_price)
                if category in category_prices:
                    category_prices[category].append(sell_value)
                else:
                    category_prices[category] = [sell_value]

for category in category_prices:
    prices = category_prices[category]
    avg_bells = sum(prices) // len(prices)
    print(f"{category}: {len(prices)} items, {avg_bells} avg. bells")



with open('animal_crossing_bell_avg.csv', 'w', newline='') as csvfile:
    fieldnames = ['Item Type', 'Buyable Items', 'Avg. Price - Bells', 'Most Expensive', 'Cheapest']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for category in category_prices:
        prices = category_prices[category]
        writer.writerow({'Item Type': category,
                         'Buyable Items': len(prices),
                         'Avg. Price - Bells': sum(prices) // len(prices),
                         'Most Expensive': max(prices),
                         'Cheapest': min(prices)})


