import re


def data_save(full_names, emails, phones, birthdays):
    save_file = input("Enter the path to save: ")
    with open(save_file, "a") as file:
        for name, email, phone, birthdate in zip(full_names, emails, phones, birthdays):
            valid = {"full_name": f"{name.group(1)} {name.group(2)}",
                     "e-mail": email.group(),
                     "phone": f"+{phone.group(1)} {phone.group(2)}-{phone.group(3)}-{phone.group(4)}",
                     "birthdate": f"{birthdate.group(1)}-{birthdate.group(2)}-{birthdate.group(3)}"}
            file.write(f"\nData: {valid}")


def data_extract(path=input("Enter the path to read: ")):
    patterns = {"full_name": re.compile(r"([A-Z][a-z]+).*?([A-Z][a-z]+)"),
                "e-mail": re.compile(r"[\w\-.]+@[A-Za-z]+\.[a-z]+"),
                "phone": re.compile(r'\+?\s?(\d{2}).*?(\d{3}).*?(\d{3}).*?(\d{3})'),
                "birthdate": re.compile(r"(\d{2})[\-/ ](\d{2})[\-/ ](\d{4})")}
    try:
        with open(path, "r") as sheet:
            file = sheet.read()
            full_names = patterns["full_name"].finditer(file)
            emails = patterns["e-mail"].finditer(file)
            phones = patterns["phone"].finditer(file)
            birthdays = patterns["birthdate"].finditer(file)
    except FileNotFoundError:
        print("File does not exist!")
    data_save(full_names, emails, phones, birthdays)


if __name__ == "__main__":
    data_extract()
