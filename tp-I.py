class check_password():
	def __init__(self, password=None):
		self.password = password
		self.level = 0

	def have_require_lenght(self):
		if len( self.password) >= 12:
			return True
		return False

	def have_lower_case(self):
		if any(c.islower() for c in self.password):
			return True
		else:
			return False

	def have_upper_case(self):
		if any(c.isupper() for c in self.password):
			return True
		else:
			return False

	def have_numeric(self):
		if any(c.isdigit() for c in self.password):
			return True
		else:
			return False

	def have_special_char(self):
		if any(c.isalnum() for c in self.password):
			return True
		else:
			return False
	def count_characters(self):
		char_count = {}

		for char in self.password:
			if char in char_count:
				char_count[char] += 1
			else:
				char_count[char] = 1

		return char_count
	def give_level(self):
		count = 0
		nbr = 0
		percent = {
			'lenght': 30,
			'upperc': 11,
			'lowerc' : 11,
			'numeric':13,
			'special_char': 25,
			'all_verified':10
		}
		if self.password.have_require_lenght():
			self.level += percent['lenght']
			count = count + 1
		if self.password.have_upper_case():
			self.level += percent['upperc']
			count = count + 1
		if self.password.have_lower_case():
			self.level += percent['lowerc']
			count = count + 1
		if self.password.have_numeric():
			self.level += percent['numeric']
			count = count + 1
		if self.password.have_special_char():
			self.level += percent['special_char']
			count = count + 1
		if count == 5:
			self.level += percent['all_verified']
		rst = self.password.count_characters()
		for y ,countn in rst.items():
			if countn > 3:
				nbr += 1
		print(rst.items())
		if nbr:
			if nbr >= 2 and nbr <= 3:
				self.level -= 7
			elif nbr >= 3:
				self.level -= 15
		print(self.level)	
		print(count)		

	def bad_object_password(self):
		pass
	
re = check_password()
re.password = check_password('q25weeeRtyuiooopassss')
print(re.password.have_require_lenght())
re.give_level()
print(re.password.count_characters())