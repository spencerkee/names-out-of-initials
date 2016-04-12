emailLocation = 'emailAddresses'
nameLocation = 'allNames'
def main(first, second, year):
	with open(emailLocation) as f: emails_names = [x.strip('\n').split(',') for x in f]
	all_emails = [x[0] for x in emails_names]
	matching_emails = list(all_emails)
	if first != '*':
		matching_emails = [x for x in matching_emails if x[0] == first]
	if second != '*':
		matching_emails = [x for x in matching_emails if x[1] == second]
	if year != '*':
		matching_emails = [x for x in matching_emails if x[len(x)-2:] == year]
	for i in matching_emails:
		print i, emails_names[all_emails.index(i)][1]

if __name__ == '__main__':
	main('*','k','*')
