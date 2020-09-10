# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"]

def convert_to_string(lst):
	string_of_list_contents = ""
	for item in lst:
		string_of_list_contents += item
	
	return string_of_list_contents

def restore_case(original_file, censored_file):
	lst1, lst2 = list(original_file), list(censored_file)
	
	for index in range(len(lst2)):
		if lst2[index] == "#":
			lst1[index] = lst2[index]
	
	case_preserved = convert_to_string(lst1)
	return case_preserved

def censor_phrase(file, illegal_phrase):
	replacement_text = "#" * len(illegal_phrase)
	clean_file = file.lower()
	clean_file = clean_file.replace(illegal_phrase, replacement_text)
	clean_file = restore_case(file, clean_file)
	return clean_file

def censor_phrase_list(file, list_of_phrases):
	censored_file = file
	sorted_list_of_phrases = sorted(list_of_phrases, key=len, reverse=True)
	for illegal_phrase in sorted_list_of_phrases:
		censored_file = censor_phrase(censored_file, illegal_phrase)
	
	return censored_file

def reduce_alarmism(file, list_of_proprietary_phrases, list_of_negative_phrases):
	censored_file = file
	to_be_censored = []
	for term in list_of_proprietary_phrases:
		to_be_censored.append(term)
	count_of_negative_terms = 0
	
	for term in list_of_negative_phrases:
		count_of_negative_terms += file.count(term)
		if count_of_negative_terms > 1:
			to_be_censored.append(term)
	
	to_be_censored_sorted = sorted(to_be_censored, key=len, reverse=True)
	censored_file = censor_phrase_list(file, to_be_censored_sorted)
	
	return censored_file

email_one = censor_phrase(email_one, "learning algorithms")
print(email_one)
print("------\n")

email_two = censor_phrase_list(email_two, proprietary_terms)
print(email_two)
print("------\n")

email_three = reduce_alarmism(email_three, proprietary_terms, negative_words)
print(email_three)
