import csv


def read_csv_and_create_2d_list(csv_file_path):
    result_2d_list = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            proxy = row[0] + ':' + row[7]
 
            result_2d_list.append(proxy)

    with open("output.txt", "w") as file:
        for element in result_2d_list:
            file.write(str(element) + "\n")

# I will take all my money from people
read_csv_and_create_2d_list('Free_Proxy_List.csv')
