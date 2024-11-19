from datetime import datetime
import pandas as pd

# Guest details
while True:
    try:
        guest_num = input('How many guests arrived: ')
        if guest_num.isdigit():  # Check if the input is a valid positive integer
            guest_num = int(guest_num)  # Convert the valid input to an integer
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Invalid input. Try again.")


guest_records = []  # List to store all guest data
catalogue = {'wine': 500, 'soap': 200, 'breakfast': 1000, 'lunch': 2000, 'supper': 2500}

# Iterate over the number of guests
for num in range(guest_num):
    guest_name = input("Guest's name: ")
    departure_time = datetime.now().strftime('%H:%M:%S')# 'HH:MM:SS' format
    departure_date = datetime.now().strftime('%Y-%m-%d')  # 'YYYY-MM-DD' format

    items_used = []

    print('-' * 15)
    space = '-' * 2
    print(f'| item  {space}  Price' )
    for item, price in catalogue.items():
        print(f"| {item} {space} Ksh {price}")
    print('-' * 15)
    
    print(f"What items were purchased by our guest {guest_name} :  (type 'done' to stop): ")
    while True:
        item_purchased=input().strip().lower()
        if item_purchased == 'done':
            break
        elif item_purchased in catalogue:
            items_used.append(item_purchased)
        else:
            print(f"Invalid item")

    total_cost = sum(catalogue[item] for item in items_used)

    # Each iteration of your loop creates a new dictionary (representing a row values)
    # Append the guest record to the list that will use to populate the DataFrame
    guest_records.append({
        'name': guest_name,
        'arrival_date': departure_date,
        'departure_time': departure_time,
        'inventory': ', '.join(items_used),  # Convert the list to a string for storage
        'total_cost': total_cost
    })

# Convert the list of guest records into a DataFrame
guest_df = pd.DataFrame(guest_records,columns=['departure_date','departure_time','name','inventory','total_cost'])


# Exporting the DataFrame to an Excel file
# guest_df.to_excel('guest_records.xlsx', index=False)

# guest_df.set_index(['arrival_date','name'], inplace=True)
print("\nGuest DataFrame:")
print(guest_df)

# Displaying receipt-like summary for each guest
for index, row in guest_df.iterrows():
    # guest_name, arrival_date = index
    print(f"Guest: {guest_name}")
    print(f"departure Date: {departure_date}")
    print(f"Inventory: {row['inventory']}")
    print(f"Total Cost: Ksh {row['total_cost']}")
    print(f"Time of Exit: {row['departure_time']}")
    print('-' * 30)


