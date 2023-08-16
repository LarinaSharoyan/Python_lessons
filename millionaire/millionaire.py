import random
import os.path

def get_random_5_questions(questions):
	tmp = []
	while len(tmp) < 5:
		num = random.randint(0, len(questions) -1)
		if questions[num] not in tmp:
			tmp.append(questions[num])
	return tmp

def structure_questions(tmp):
	gquestions = {}
	for el in tmp:
		q, a = el.split("?")
		gquestions[q] = a.split(",")
	return gquestions

def game(gquestions):
	cnt = 0
	opt = ['50/50', 'help from the friend', 'help from the hall']
	for q, a in gquestions.items():
		print(q)
		correct = a[0]
		random.shuffle(a)
		for el in a:
			print(el)
		if len(opt) != 0:
			print("You also can use these opportunities")
			for i in opt:
				print(f'{opt.index(i) +1}. {i}')
		answer = input("Enter your answer or option: ")
		if answer in opt and answer == "50/50":
			opt.remove(opt[0])
			if fifty_fifty(a, correct):
				print("Correct")
				cnt += 1
			else:
				print("Incorrect. The correct answer was", correct)
		elif answer in opt and answer.lower() == "help from the hall":
			opt.remove('help from the hall')
			if help_hall(a, correct):
				print("Correct")
				cnt += 1
			else:
				print("Incorrect. The correct answer was", correct)
		elif answer in opt and answer.lower() == "help from the friend":
			opt.remove('help from the friend')
			print(f"Yes, the correct answer is {correct}")
			cnt += 1
		elif answer.lower() == correct:
			print("Correct")
			cnt += 1
		else:
			print("Incorrect. The correct answer was", correct)

	print("You got %d/5" %cnt)
	return cnt

def get_questions_from_file(fname):
	with open(fname) as f:
		return f.readlines()

def sanitize_data(ml):
	return [el.strip() for el in ml]

def check_file_existence(fname):
	if not os.path.isfile(fname):
		print("Your files does not exists: %s. Please check" %fname)
		return False
	return True

def get_top_players_from_file(fname):
	with open(fname) as f:
		return f.readlines()

def create_file(fname):
	f = open(fname, "w")
	f.close()

def create_players_dict(data):
	# should be written "username: XP"
	md = {}
	for el in data:
		p,x = el.split(": ")
		md[p] = int(x)
	return md

def confirm_username(username, players):	
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
	ml = list(players.items())
	ml.sort(key=lambda x: x[1], reverse=True)
	return ml

def write_player_xp(fname, ml):
	with open(fname, "w") as f:
		for pl, xp in ml:
			f.write(pl + ": " + str(xp) + "\n")

def fifty_fifty(list_of_answers, correct_ans):
	list_of_answers.remove(correct_ans)
	random.shuffle(list_of_answers)
	ans = input(f"{correct_ans} or {list_of_answers[0]}: ")
	return ans == correct_ans

def help_friend(correct):
	return correct

import random

def help_hall(list_options, correct_answer):
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
				x = random.randint(0, 15)
				cnt.append(x)
				dct[list_options[i]] = x
	print(dct)
	ans = input("Enter the answer: ")
	return ans == correct_answer


def main():
	username = input("Enter your username: ")
	question_file = "questions.txt"
	fl = check_file_existence(question_file)
	if not fl:
		exit()
	top_file = "top_players.txt"
	fl = check_file_existence(top_file)
	if not fl:
		create_file(top_file)
	players_data = get_top_players_from_file(top_file)
	players = sanitize_data(players_data)
	players_dict = create_players_dict(players)
	username = confirm_username(username, players_dict)
	questions = get_questions_from_file(question_file)
	questions = sanitize_data(questions)
	random5 = get_random_5_questions(questions)
	game_questions = structure_questions(random5)
	xp = game(game_questions)
	players_dict[username] = xp
	players = sort_players_by_xp(players_dict)
	write_player_xp(top_file, players)


main()





