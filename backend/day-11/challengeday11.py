def write_file(sort_name: list):
    # with open("names.txt", "w") as file:
    with open("C:\\Users\\JE\\Desktop\\Program\\AWSCC-CodeQuest-Backend\\backend\\day-11\\names.txt", "w") as file:
        file.writelines(sort_name)


def sort_list(name: list) -> list:
    return sorted(name)


def read_file() -> list:
    # with open("names.txt", "r") as file:
    with open("C:\\Users\\JE\\Desktop\\Program\\AWSCC-CodeQuest-Backend\\backend\\day-11\\names.txt", "r") as file:
        name_list = file.readlines()
    return name_list


def main():
    name_list = read_file()
    name_list_sort = sort_list(name_list)
    write_file(name_list_sort)


main()