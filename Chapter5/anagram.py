def are_anagrams(word1, word2):
	"""2. Return True, if wordds are anagrams."""
	#Sort the characters of the word.
	word1_sorted = sorted(word1)	#3. sorted returns a sorted list
	word2_sorted = sorted(word2)
	
	#Check that the sorted words are identical
	return word1_sorted == word2_sorted
	
print ("Anagram Test")

#1. Input 2 words
two_words = input ("Enter two space separated words :")
word1,word2 = two_words.split()	#split into list of words

if are_anagrams(word1, word2):
	print("The words are anagram")
else :
	print("The words area not anagram")
