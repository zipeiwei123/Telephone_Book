from ...telephone.phone import *
import unittest


class My_Test(unittest.TestCase):

	def test_decoding(self):
		number = '1-765-432-7890'
		phone_obj = Telephone_Book(number)
		self.assertEqual(phone_obj.decoding(), '17654327890')


	# def test_words_to_numbers(self):
	# 	number = '1-765-58-CATS'
	# 	phone_obj = Telephone_Book(number)


if __name__ == '__main__':
	unittest.main()