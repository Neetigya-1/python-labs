print("Neetigya,24bee113")
import csv
data = [
    ["Name", "Age", "City"],
    ["Neetigya", 30, "Mumbai"],
    ["Saurav", 25, "Jaipur"],
    ["Eklavya", 35, "Chennai"]
]
file_path = "output.csv"
with open(file_path, mode='w', newline='',) as file:
    writer = csv.writer(file)
    writer.writerows(data)
