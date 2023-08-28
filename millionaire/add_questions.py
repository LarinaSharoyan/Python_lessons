def ask():
    add = input('Would you like to add questions?: ')
    return add.lower() == "yes" or add.lower() == "y"
def add_line():
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
def return_lines(file):
    with open(file) as f:
        return f.readlines()
def check_qst_existence(lst, line):
    for i in lst:
        if line.split('?')[0] == i.split('?')[0]:
            return False
        return True
def file_append(file, line):
    try:
        with open(file, 'a') as fl:
            fl.write(line+'\n')
    except:
        print("Your file does not exist. Please check")
        exit()
def main():
    if ask():
        mstr = add_line()
        if add_line():
            file_append('qst.txt', mstr)
main()
            

