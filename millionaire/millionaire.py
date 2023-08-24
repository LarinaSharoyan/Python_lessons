"""
random is for shuffling list of questions
os.path is for checking file existence
sys is for exit()
"""
import random
import os.path
import sys

def get_random_5_questions(questions):
    """Getting random questions from file"""
    tmp = []
    while len(tmp) < 5:
        num = random.randint(0, len(questions) -1)
        if questions[num] not in tmp:
            tmp.append(questions[num])
    return tmp

def structure_questions(tmp):
    """Structuring, spliting all 5 questions"""
    gquestions = {}
    for element in tmp:
        quest, ans = element.split("?")
        gquestions[quest] = ans.split(",")
    return gquestions

def game(gquestions):
    """Main logic of the game"""
    cnt = 0
    opt = ['50/50', 'help from the friend', 'help from the hall']
    option_functions = {
        '50/50': fifty_fifty,
        'help from the friend': help_friend,
        'help from the hall': help_hall
    }

    for quest, ans in gquestions.items():
        print(quest)
        correct = ans[0]
        random.shuffle(ans)
        for elem in ans:
            print(elem)

        if opt:
            print("You also can use these opportunities")
            for i, option in enumerate(opt, start=1):
                print(f'{i}. {option}')

        answer = input("Enter your answer or option: ")
        if answer in option_functions:
            option_function = option_functions[answer]
            opt.remove(answer)
            if option_function(ans, correct):
                print("Correct")
                cnt += 1
            else:
                print("Incorrect. The correct answer was", correct)
        elif answer.lower() == correct:
            print("Correct")
            cnt += 1
        else:
            print(f"Incorrect. The correct answer was {correct}")

    print(f"You got {cnt}")
    return cnt

def get_questions_from_file(fname):
    """Gets questions from given file"""
    with open(fname, encoding='utf-8') as file:
        return file.readlines()

def sanitize_data(my_list):
    """Remove all new lines"""
    return [el.strip() for el in my_list]

def check_file_existence(fname):
    """Checks if given file exists or not"""
    if not os.path.isfile(fname):
        print(f"Your files does not exists: {fname}. Please check")
        return False
    return True

def get_top_players_from_file(fname):
    """Top players"""
    with open(fname, encoding='utf-8') as file:
        return file.readlines()

def create_file(fname):
    """Creates a file"""
    with open(fname, "w", encoding='utf-8') as file:
        file.close()

def create_players_dict(data):
    """Creates dictionary for all top players"""
    # should be written "username: XP"
    my_dict = {}
    for elem in data:
        player, points = elem.split(": ")
        my_dict[player] = int(points)
    return my_dict

def confirm_username(username, players):
    """Asks for username"""
    if username in players:
        ans = input("Would you like to rewrite your XP? ")
        if ans.lower() == "y":
            pass
        else:
            username = input("Enter your username: ")
            while username in players:
                username = input("Enter your username: ")
    return username

def sort_players_by_xp(players):
    """Sorts all players by score"""
    mlist = list(players.items())
    mlist.sort(key=lambda x: x[1], reverse=True)
    return mlist

def write_player_xp(fname, mlist):
    """Writes all top players in the file"""
    with open(fname, "w", encoding='utf-8') as file:
        for player, points in mlist:
            file.write(player + ": " + str(points) + "\n")

def fifty_fifty(list_of_answers, correct_ans):
    """fifty-fifty option logic"""
    list_of_answers.remove(correct_ans)
    random.shuffle(list_of_answers)
    ans = input(f"{correct_ans} or {list_of_answers[0]}: ")
    return ans == correct_ans

def help_friend(correct):
    """help form the friend logic"""
    return correct

def help_hall(list_options, correct_answer):
    """help from the hall logic"""
    dct = {}
    cnt = []
    correct_value = random.randint(50, 70)
    for i in range(4):
        if list_options[i] == correct_answer:
            dct[list_options[i]] = correct_value
        else:
            if len(cnt) == 2:
                dct[list_options[i]] = 100 - correct_value - sum(cnt)
            else:
                random_number = random.randint(0, 15)
                cnt.append(random_number)
                dct[list_options[i]] = random_number
    print(dct)
    ans = input("Enter the answer: ")
    return ans == correct_answer


def main():
    """All functions here!"""
    username = input("Enter your username: ")
    question_file = "questions.txt"
    file_check = check_file_existence(question_file)
    if not file_check:
        sys.exit()
    top_file = "top_players.txt"
    file_check = check_file_existence(top_file)
    if not file_check:
        create_file(top_file)
    players_data = get_top_players_from_file(top_file)
    players = sanitize_data(players_data)
    players_dict = create_players_dict(players)
    username = confirm_username(username, players_dict)
    questions = get_questions_from_file(question_file)
    questions = sanitize_data(questions)
    random5 = get_random_5_questions(questions)
    game_questions = structure_questions(random5)
    exper_points = game(game_questions)
    players_dict[username] = exper_points
    players = sort_players_by_xp(players_dict)
    write_player_xp(top_file, players)


main()
