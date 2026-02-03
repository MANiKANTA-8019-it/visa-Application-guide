import json
import os

DATA_PATH = os.path.join("src", "data", "visa_rules.json")


def load_visa_rules():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def get_user_input():
    country = input("Enter destination country: ").strip()
    purpose = input("Enter purpose (Study / Work / Tourist): ").strip()
    return country, purpose


def find_matching_visa(country, purpose, rules):
    if country not in rules:
        return None, None

    for visa_type, visa_data in rules[country].items():
        if visa_data["purpose"].lower() == purpose.lower():
            return visa_type, visa_data

    return None, None


def display_visa_info(country, visa_type, visa_data):
    print("\n✅ Visa Match Found")
    print(f"Country: {country}")
    print(f"Visa Type: {visa_type}")

    print("\n📄 Required Documents:")
    for doc in visa_data["documents"]:
        print(f"- {doc}")

    print(f"\n⏳ Processing Time: {visa_data['processing_time']}")

    print("\n⚠️ Common Rejection Reasons:")
    for reason in visa_data["common_rejections"]:
        print(f"- {reason}")


def main():
    print("🌍 Visa Application Guide\n")

    rules = load_visa_rules()
    country, purpose = get_user_input()

    visa_type, visa_data = find_matching_visa(country, purpose, rules)

    if not visa_type:
        print("\n❌ No matching visa found for your input.")
        return

    display_visa_info(country, visa_type, visa_data)


if __name__ == "__main__":
    main()
