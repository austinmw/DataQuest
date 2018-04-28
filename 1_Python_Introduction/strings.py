vocabulary = open("dictionary.txt").read()
tokenized_vocabulary = vocabulary.split(' ')
print(tokenized_vocabulary[0:4])





f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")

story_string = story_string.replace("'","")
story_string = story_string.replace(";","")
story_string = story_string.replace("\n","")
