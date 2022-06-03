from csv import reader, writer, DictReader, DictWriter
from dataclasses import field
with open("players.csv", "w", newline="") as csvFile:
    fields=[
        "Id",
        "Name",
        "Team",
        "Age",
        "Height",
        "Weight"
    ]
    dWriter = DictWriter(csvFile,fieldnames=fields)
    dWriter.writeheader()
    dWriter.writerow({
            "Id":1,
            "Name":"Micheal Jordan",
            "Team":"CHI",
            "Age":35.0,
            "Height":198.12,
            "Weight":97.97
        })