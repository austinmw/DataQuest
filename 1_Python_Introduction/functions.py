

def clean_text(text_string, special_characters):
	cleaned_string = text_string
	for string in special_characters:
		cleaned_string = cleaned_string.replace(string, "")
	cleaned_string = cleaned_string.lower()
	return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
	cleaned_text = text_string
	if clean:
		cleaned_text = clean_text(text_string, special_characters)
	tokens = cleaned_text.split(" ")
	return(tokens)

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
	misspelled_words = []
	vocab = open(vocabulary_file).read()
	text = open(text_file).read()
	tokenized_vocabulary = tokenize(vocabulary, special_characters)
	tokenized_text = tokenize(text, special_characters, True)
	for w in tokenized_text:
		if w not in tokenized_vocabulary and w != '':
			misspelled_words.append(w)
	return misspelled_words


final_misspelled_words = []
final_misspelled_words = spell_check("dictionary.txt","story.txt")
print(final_misspelled_words)

