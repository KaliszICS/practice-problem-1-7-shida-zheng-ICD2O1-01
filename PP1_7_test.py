import os.path
import sys
import PP1_7

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	PP1_7.q1()
	captured = capsys.readouterr()
	assert captured.out == "True\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["4"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: False\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["b"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input the letter a: False\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["zebra"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a word earlier in the dictionary than google: False\n"

def test_q5_1(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["5", "5"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input another integer: Your numbers multiplied together are greater than 40: False\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()


	PP1_7.q1()
	captured = capsys.readouterr()
	assert captured.out == "True\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["5"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: False\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["a "]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input the letter a: False\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["google"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a word earlier in the dictionary than google: False\n"

def test_q5_2(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["8", "5"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input another integer: Your numbers multiplied together are greater than 40: False\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	PP1_7.q1()
	captured = capsys.readouterr()
	assert captured.out == "True\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["6"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: True\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["a"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input the letter a: True\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["elementary"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a word earlier in the dictionary than google: True\n"

def test_q5_3(capsys):

	try:
		exists = os.path.exists("PP1_7.py")
		assert exists
	except:
		sys.exit()

	input_values = ["8","8"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_7.input = mock_input

	PP1_7.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input an integer: Input another integer: Your numbers multiplied together are greater than 40: True\n"

