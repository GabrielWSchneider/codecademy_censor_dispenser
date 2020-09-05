# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def redact_message(file, message):
	censored_file = file.split(message)
	censored_file = "<redacted>".join(censored_file)
	
	return censored_file

def redact_phrases(file, list_of_phrases):
	censored_file = file
	for illegal_phrase in list_of_phrases:
		censored_file = redact_message(censored_file, illegal_phrase)
	
	return censored_file

email_one = redact_message(email_one, "learning algorithms")
print(email_one)
print("------\n")

email_two = redact_phrases(email_two, proprietary_terms)
print(email_two)
