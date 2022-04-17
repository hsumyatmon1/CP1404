def main():
    emails = []
    names = []
    email = input("Email: ")
    while email != "":
        emails.append(email)
        full_name = get_name(email)
        names.append(full_name)
        email = input("Email: ")

    name_and_email = dict(zip(names, emails))

    for full_name in name_and_email:
        print("{} ({})".format(full_name, name_and_email[full_name]))


def get_name(email):
    split_email = email.split('@')
    name = split_email[0].split('.')
    if len(name) > 1:
        full_name = (name[0] + ' ' + name[1]).title()
    else:
        full_name = name[0].title()

    conformation = input("Is your name {}? (Y/n) ".format(full_name)).lower()
    if conformation == 'n' or conformation == 'no':
        full_name = input("Name: ").title()

    return full_name


if __name__ == '__main__':
    main()
