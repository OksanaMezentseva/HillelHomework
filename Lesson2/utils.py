from faker import Faker

fake = Faker()


def generate_names(quantity: int) -> list:
    name_list = []
    for _ in range(quantity):
        full_name = fake.name()
        name = full_name.split()[0]
        name_list.append(name)
    return name_list


def generate_emails(quantity: int) -> list:
    emails_list = []
    for _ in range(quantity):
        emails_list.append(fake.email())
    return emails_list

