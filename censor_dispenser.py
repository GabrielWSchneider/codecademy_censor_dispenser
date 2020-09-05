# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def redact_message(file, message):
	censored_file = file.split(message)
	censored_file = "<redacted>".join(censored_file)
	
	return censored_file

email_one = redact_message(email_one, "learning algorithms")
print(email_one)
