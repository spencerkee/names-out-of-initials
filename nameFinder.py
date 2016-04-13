import sys

def write_ldap_data(ldap_filename, writing_filename):
	with open(ldap_filename) as f: #read in ldap file
		data = f.read()

	data = data.split('\n\n')#split it into a block for every person
	new_data = []
	valid_years = ['12', '13', '14', '15', '17']

	for i in data:
		data_block = str(i)
		data_block = data_block.split('\n')
		personal_information = [[],[]]
		for j in data_block:
			if 'uid:' in j and j[len(j)-2:] in valid_years:#if uid ends with a possible year
				personal_information[0] = j.split(': ')[1]
			if 'cn:' in j:#name
				personal_information[1] = j.split(': ')[1]
		#if the block contains a uid and cn of the correct format, save it
		if not any(x == [] for x in personal_information) and len(personal_information) >= 2:
			new_data.append(personal_information)

	open(writing_filename, 'w').close()#empty writing file
	with open(writing_filename, 'a') as f:#write information to filename
		for i in new_data:
			string = i[0] + ', '+ i[1] + '\n'
			f.write(string)

def main(first, second, year):
	if all(x == 0 for x in [len(first), len(second), len(year)]):
		sys.exit('No terms')
	if any(x > 1 for x in [len(first), len(second)]) or len(year) > 2:
		sys.exit('Input term too large')

	#uid_names contains data in the form 'uid, name'
	with open(formatted_data_location) as f: uid_names = [x.strip('\n').split(',') for x in f]
	all_uid = [x[0] for x in uid_names]
	matching_uid = list(all_uid)
	#reduce the possible uid for every criterea
	if first != '':
		matching_uid = [x for x in matching_uid if x[0] == first]
	if second != '':
		matching_uid = [x for x in matching_uid if x[1] == second]
	if year != '':
		matching_uid = [x for x in matching_uid if x[len(x)-2:] == year]
	
	if len(matching_uid) == 0:
		sys.exit('No match')
	else:
		for i in matching_uid:
			print i, uid_names[all_uid.index(i)][1]

if __name__ == '__main__':
	formatted_data_location = 'emailAddresses'
	write_ldap_data('ldap_data', formatted_data_location)
	main('a','f','')
