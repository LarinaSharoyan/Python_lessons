"""
    argparse is for arguments when we run program
    webbrowser to open index.html
    os is to find index.html location
    sys is just for sys.exit()
    xlsxwriter to create an excel file and write data in it
    pandas is to convert excel to html
"""
import argparse
import webbrowser
import os
import sys
import xlsxwriter
import pandas

def check_subpocess():

def check_file_existence(fname):
    """ Checks file exists or not"""
    if not os.path.isfile(fname):
        print(f"Your file does not exists: {fname}. Please check")
        sys.exit()

def open_data(filename):
    try:
        """Opens data.txt and returns all lines in list"""
        with open(filename, encoding='utf-8') as file:
            return file.readlines()
        file.close()
    except:
        print(f'Your file does not exist: {filename}. Please check.')
        sys.exit()

def create_list_of_dct(filename):
    """Gets that list and creates a list of dictionaries"""
    lst = []
    for i in filename:
        line = i.strip().split()
        dct = {}
        dct['name'] = line[0]
        dct['surname'] = line[1]
        dct['age'] = line[2]
        dct['profession'] = line[3]
        lst.append(dct)
    return lst

def sort_lst(lst, filter_):
    """Sorts that list of dicts by given filter"""
    return sorted(lst, key=lambda x: x[filter_])

def create_excel_file(data, f_name):
    try:
    
        """Creates an excel file and writes all data here"""
        workbook = xlsxwriter.Workbook(f_name)
        worksheet = workbook.add_worksheet()
        bold_yellow_bg = workbook.add_format({
            'bold': True,
            'bg_color': 'yellow',
            'align': 'center',
            'valign': 'vcenter'
            })
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
    except:
        print("")

def get_args():
    """Gets all arguments during runtime"""
    parser = argparse.ArgumentParser(description=\
            'Input, output files and also you can add by what do you wanna filter your data')
    parser.add_argument('-f', '--input-file', required=True, help='Input file name')
    parser.add_argument('-o', '--output-file', required=True, help='Output file name')
    parser.add_argument('filter', nargs='?', default='name',\
            choices=['name', 'surname', 'age', 'profession'],  help='Filter by what(default=name)')
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    filter_ = args.filter
    return [input_file, output_file, filter_]

def convert_to_website(filename):
    """Converts that excel file to website"""
    file_r= pandas.read_excel(filename)
    table = file_r.to_html(index=False)
    html_filename = 'index.html'
    with open(html_filename, 'w', encoding='utf-8') as html:
        html.write(table)
    current_dir = os.getcwd()
    quest = input('Do you wanna see the website?:')
    if quest.lower() == 'yes':
        webbrowser.open(current_dir + '/index.html')

def main():
    """All functions here"""
    args = get_args()
    data_file = args[0]
    excel_file = args[1]
    filter_by_what = args[2]
    check_file_existence(data_file)
    data = open_data(data_file)
    lst = create_list_of_dct(data)
    sorted_lst = sort_lst(lst, filter_by_what)
    create_excel_file(sorted_lst, excel_file)
    convert_to_website(excel_file)
main()
