import pandas as pd

print("=" * 60)
print("AQI SEARCH & RETRIEVAL SYSTEM")
print("=" * 60)

# Load processed dataset
df = pd.read_csv("data/processed/physics_validated_dataset.csv")

# Convert Datetime column
df["Datetime"] = pd.to_datetime(df["Datetime"])

while True:

    print("\nSearch Options")
    print("1. Search by Station ID")
    print("2. Search by AQI Range")
    print("3. Search by City")
    print("4. Show Dataset Summary")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # -----------------------------
    # Search by Station
    # -----------------------------
    if choice == "1":

        station = input("Enter Station ID: ").strip()

        result = df[df["StationId"] == station]

        print("\nRecords Found:", len(result))

        print(result.head())

    # -----------------------------
    # AQI Range
    # -----------------------------
    elif choice == "2":

        low = float(input("Minimum AQI: "))
        high = float(input("Maximum AQI: "))

        result = df[
            (df["AQI"] >= low) &
            (df["AQI"] <= high)
        ]

        print("\nRecords Found:", len(result))

        print(result.head())

    # -----------------------------
    # City Search
    # -----------------------------
    elif choice == "3":

        city = input("Enter City Name: ").strip()

        result = df[
            df["City"].str.lower() == city.lower()
        ]

        print("\nRecords Found:", len(result))

        print(result.head())

    # -----------------------------
    # Dataset Summary
    # -----------------------------
    elif choice == "4":

        print("\nDataset Shape:", df.shape)

        print("\nStations:", df["StationId"].nunique())

        print("Cities:", df["City"].nunique())

        print("Average AQI:", round(df["AQI"].mean(),2))

        print("Maximum AQI:", round(df["AQI"].max(),2))

    # -----------------------------
    # Exit
    # -----------------------------
    elif choice == "5":

        print("\nThank you!")

        break

    else:

        print("Invalid Choice.")