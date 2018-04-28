# open or overwrite file, write data, skip to top, print
with open('somefile.txt', 'w+') as f:
	# Note that f has now been truncated to 0 bytes, so you'll only
	# be able to read data that you wrote earlier...
	f.write('somedata\n')
	f.seek(0)  # Important: return to the top of the file before reading, otherwise you'll just read an empty string
	data = f.read() # Returns 'somedata\n'
	print(data)

""" 
Here is a list of the different modes of opening a file:

	r

	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
	rb

	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
	r+

	Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
	rb+

	Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.
	w

	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
	wb

	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
	w+

	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
	wb+

	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
	a

	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
	ab

	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
	a+

	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
	ab+

	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
"""
