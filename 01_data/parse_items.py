filename = "animal_crossing_items.tsv"
filename = "animal_crossing_items.csv"

f = open(filename, "r")
for line in f.readlines():
  if len(line.split("\t")) != 16:
    print(len(line.split("\t")))
    print(line)





filename = "animal_crossing_items.csv"

import csv





def return_bell_profit(row):
    if row[6] != "bells" or row[8] != "bells":
        return 1000
    if not (row[5].isnumeric() and row[7].isnumeric()):
        return 1000
    return int(row[7]) / int(row[5])


min_profit = 1000
min_row = None

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
    print(f"{category}: {len(prices)} items, {sum(prices)/len(prices)} avg")

