emailLocation = 'emailAddresses'

def write_ldap_data(filename): #some people have multiple give names
	with open(filename) as f: 
		data = f.read()

	data = data.split('\n\n')
	# print len(data)
	new_data = []
	valid_years = ['12', '13', '14', '15', '17']

	for i in data:
		data_block = str(i)
		data_block = data_block.split('\n')
		personal_information = [[],[]]
		for j in data_block:
			if 'uid:' in j and j[len(j)-2:] in valid_years:
				personal_information[0] = j.split(': ')[1]
			if 'cn:' in j:
				personal_information[1] = j.split(': ')[1]
		if not any(x == [] for x in personal_information) and len(personal_information) >= 2:
			new_data.append(personal_information)

	print len(new_data)

	open(emailLocation, 'w').close()
	with open(emailLocation, 'a') as f:
		for i in new_data:
			string = i[0] + ', '+ i[1] + '\n'
			f.write(string)

def main(first, second, year):
	with open(emailLocation) as f: emails_names = [x.strip('\n').split(',') for x in f]
	all_emails = [x[0] for x in emails_names]
	matching_emails = list(all_emails)
	if first != '*':
		matching_emails = [x for x in matching_emails if x[0] == first]
	print len(matching_emails)
	if second != '*':
		matching_emails = [x for x in matching_emails if x[1] == second]
	print len(matching_emails)
	if year != '*':
		matching_emails = [x for x in matching_emails if x[len(x)-2:] == year]
	print len(matching_emails)
	for i in matching_emails:
		print i, emails_names[all_emails.index(i)][1]

if __name__ == '__main__':
	write_ldap_data('ldap_data')
	main('s','k','*')
