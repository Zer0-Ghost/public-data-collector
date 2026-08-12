import requests
import csv
import os

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "users.csv"


def collect_users():
    print("\nConnecting to API...")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        users = response.json()

    except requests.RequestException as error:
        print(f"❌ Could not collect data: {error}")
        return

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Username",
            "Email",
            "Phone",
            "Website",
            "City",
            "Company"
        ])

        for user in users:
            writer.writerow([
                user["name"],
                user["username"],
                user["email"],
                user["phone"],
                user["website"],
                user["address"]["city"],
                user["company"]["name"]
            ])

    print(f"\n✅ Successfully collected {len(users)} users.")
    print(f"📁 Data saved to: {OUTPUT_FILE}")


def search_users():
    if not os.path.exists(OUTPUT_FILE):
        print("\n❌ No data found. Collect users first.")
        return

    search = input("\nSearch by name, email, city, or company: ").strip().lower()

    found = False

    with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("\n===== SEARCH RESULTS =====")

        for user in reader:
            searchable_data = " ".join(user.values()).lower()

            if search in searchable_data:
                print(
                    f'{user["Name"]} | '
                    f'{user["Email"]} | '
                    f'{user["City"]} | '
                    f'{user["Company"]}'
                )
                found = True

    if not found:
        print("❌ No matching users found.")


def main():
    while True:
        print("\n==============================")
        print("     PUBLIC DATA COLLECTOR")
        print("==============================")
        print("1. Collect users")
        print("2. Search users")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            collect_users()

        elif choice == "2":
            search_users()

        elif choice == "3":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n❌ Invalid option. Choose 1-3.")


if __name__ == "__main__":
    main()