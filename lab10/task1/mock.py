import random
import csv


def generate_random_phone():
    area_code = random.randint(200, 999)
    prefix = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    return f"{area_code} {prefix} {line_number}"


def generate_random_full_name():
    # List of common first names
    first_names = [
        "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael",
        "Linda", "William", "Elizabeth", "David", "Susan", "Richard", "Jessica",
        "Joseph", "Sarah", "Thomas", "Karen", "Charles", "Nancy", "Christopher",
        "Lisa", "Daniel", "Margaret", "Matthew", "Betty", "Anthony", "Sandra",
        "Mark", "Ashley", "Donald", "Kimberly", "Steven", "Emily", "Paul",
        "Donna", "Andrew", "Michelle", "Joshua", "Carol", "Kenneth", "Amanda",
        "Kevin", "Dorothy", "Brian", "Melissa", "George", "Deborah", "Timothy"
    ]

    # List of common last names
    last_names = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
        "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White",
        "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
        "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King",
        "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez",
        "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner",
        "Torres", "Parker", "Collins", "Edwards", "Stewart", "Flores", "Morris"
    ]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"


def generate_csv(filename, num_records):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user', 'phone'])

        for _ in range(num_records):
            full_name = generate_random_full_name()
            phone = generate_random_phone()
            writer.writerow([full_name, phone])

    print(f"Generated {num_records} records in {filename}")


if __name__ == "__main__":
    output_file = "random_contacts.csv"
    num_records = 100

    try:
        user_num = input("How many records do you want to generate? (press Enter for default 100): ")
        if user_num.strip():
            num_records = int(user_num)

        user_file = input(f"Enter filename (press Enter for default '{output_file}'): ")
        if user_file.strip():
            output_file = user_file
            if not output_file.endswith('.csv'):
                output_file += '.csv'
    except ValueError:
        print("Invalid number, using default value of 100 records.")

    generate_csv(output_file, num_records)