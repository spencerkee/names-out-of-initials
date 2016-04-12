emailLocation = 'emailAddresses'
nameLocation = 'allNames'
def main(first, second, year):
	with open(emailLocation) as f: all_emails = [x.strip('\n') for x in f if x != '\n']
	matchingEmails = list(all_emails)
	if first != '*':
		matchingEmails = [x for x in matchingEmails if x[0] == first]
	if second != '*':
		matchingEmails = [x for x in matchingEmails if x[1] == second]
	if year != '*':
		matchingEmails = [x for x in matchingEmails if x[len(x)-2:] == year]
	# return matchingEmails


if __name__ == '__main__':
	print main('*','k','*')
