# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "concerning", "horrible", "horribly", "questionable"]

def redact_message(file, message):
	censored_file = file.replace(message, "<redacted>")
	
	return censored_file

def redact_phrases(file, list_of_phrases):
	censored_file = file
	for illegal_phrase in list_of_phrases:
		censored_file = redact_message(censored_file, illegal_phrase)
	
	return censored_file

def reduce_alarmism(file, list_of_proprietary_phrases, list_of_negative_phrases):
	censored_file = file
	to_be_censored = list_of_proprietary_phrases
	count_of_negative_terms = 0
	
	for term in list_of_negative_phrases:
		count_of_negative_terms += file.count(term)
		if count_of_negative_terms > 1:
			to_be_censored.append(term)
	
	censored_file = redact_phrases(file, to_be_censored)
	
	return censored_file

email_one = redact_message(email_one, "learning algorithms")
print(email_one)
print("------\n")

email_two = redact_phrases(email_two, proprietary_terms)
print(email_two)
print("------\n")

email_three = reduce_alarmism(email_three, proprietary_terms, negative_words)
print(email_three)
