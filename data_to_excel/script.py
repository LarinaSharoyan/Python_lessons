import os.path
import xlsxwriter
import argparse

def check_file_existence(fname):
    if not os.path.isfile(fname):
        print("Your files does not exists: %s. Please check" %fname)
        exit()

def open_data(file):
    with open(file) as f:
        return f.readlines()
    file.close()

def create_list_of_dct(f):
    lst = []
    for i in f:
        line = i.strip().split()
        dct = {}
        dct['name'] = line[0]
        dct['surname'] = line[1]
        dct['age'] = line[2]
        dct['profession'] = line[3]
        lst.append(dct)
    return lst

def sort_lst(lst, filter):
    return sorted(lst, key=lambda x: x[filter])

def create_excel_file(data, f_name):
    workbook = xlsxwriter.Workbook(f_name)
    worksheet = workbook.add_worksheet()
    
    bold_yellow_bg = workbook.add_format({'bold': True, 'bg_color': 'yellow'})
    green_bg = workbook.add_format({'bg_color': 'green'})
    for i in range(4):
        worksheet.set_column(i, i, 15)  # Column 0 (A) width set to 15
    worksheet.write(0, 0, 'Name', bold_yellow_bg)
    worksheet.write(0, 1, 'Surname', bold_yellow_bg)
    worksheet.write(0, 2, 'Age', bold_yellow_bg)
    worksheet.write(0, 3, 'Profession', bold_yellow_bg)
    row = 1
    keys = ['name', 'surname', 'age', 'profession']
    for i in data:
        for j in range(len(i)):
            if int(i['age']) > 35:
                worksheet.write(row, j, i[keys[j]], green_bg)
            else:
                worksheet.write(row, j, i[keys[j]])
        row += 1
    workbook.close()

def get_args():
    parser = argparse.ArgumentParser(description='Input, output files and also you can add by what do you wanna filter your data')
    parser.add_argument('-f', '--input-file', required=True, help='Input file name')
    parser.add_argument('-o', '--output-file', required=True, help='Output file name')
    parser.add_argument('filter', nargs='?', default='name', choices=['name', 'surname', 'age', 'profession'],  help='Filter by what(default=name)')
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    filter_ = args.filter
    return [input_file, output_file, filter_]


def main():
    args = get_args()
    data_file = args[0]
    excel_file = args[1] 
    filter_by_what = args[2]
    check_file_existence(data_file)
    data = open_data(data_file)
    lst = create_list_of_dct(data)
    sorted_lst = sort_lst(lst, filter_by_what)
    create_excel_file(sorted_lst, excel_file)
main()
