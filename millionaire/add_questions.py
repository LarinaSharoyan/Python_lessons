"""This program is part of millionaire for operator,
it asks about to add new questions and options"""
import sys

def ask():
    """Ask if user wants to add new questions"""
    add = input('Would you like to add questions?: ')
    return add.lower() == "yes" or add.lower() == "y"
def add_line():
    """asks for question, options, correct answer and returns"""
    qst = input('enter your question: ')
    while qst[-1] != '?':
        print("In the end of the question please add ? sign")
        qst = input('enter your question: ')
    correct = input('enter your correct answer')
    options = input("""Enter your options like this
(correct,wrong,wrong,wrong) """)
    while len(options.split(',')) != 4 or options.split(',')[0].lower() != correct.lower():
        options = input("""Please Enter your options like this
("correct,wrong,wrong,wrong"): """)
    return qst+options.strip()
def return_lines(filename):
    """returns all questions that exist"""
    try:
        with open(filename, encode='utf-8') as file:
            return file.readlines()
    except FileExistsError:
        print("There's no such a file. Please check")
        sys.exit()
def check_qst_existence(lst, line):
    """check if given question exists or not"""
    for quest in lst:
        if line.split('?')[0] == quest.split('?')[0]:
            return False
    return True
def file_append(file, line):
    """writes the new question in the file"""
    try:
        with open(file, 'a', encode='utf-8') as fl:
            fl.write(line+'\n')
    except:
        print("Your file does not exist. Please check")
        sys.exit()
def main():
    """asks for adding and does appropriate functions"""
    if ask():
        mstr = add_line()
        if check_qst_existence(return_lines("qst.txt"), mstr):
            file_append('qst.txt', mstr)
        else:
            print('sorry, same question already exists')
main()
