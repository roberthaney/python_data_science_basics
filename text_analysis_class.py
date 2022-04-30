import sys

# create class
class analyzedText(object):
	# constructor with text modifiers
	def __init__ (self, text):
		formattedText = text.replace(".", "").replace(",", "").replace("?", "").replace("!", "")
		formattedText = formattedText.lower()
		self.fmtText = formattedText

	def FreqAll(self):
		self.temp = self.fmtText.split()
		self.words = {}
		for word in self.temp:
			if word not in self.words:
				self.words[word] = 1
			else:
				self.words[word] += 1
		return self.words

	def FreqOf(self, word):
		# generate word dictionary if methods not called already
		freqDict = self.FreqAll()
		# retrun value if found
		return freqDict[word] or False

# testing constructor
print "Constructor:"
def testMsg(passed):
	if passed:
		return "Test Passed"
	else:
		return "Test Failed"

try:
	samplePassage = analyzedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
	# access attribute to check 
	# print samplePassage.fmtText
	print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
	print("Error detected. Recheck your function")

# testing methods
sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

print "FreqAll Method:"
try:
	wordMap = samplePassage.FreqAll()
	print(testMsg(wordMap == sampleMap))
except:
	print("\nError detected. Recheck your function")

print "FreqOf Method"

try:
	passed = True
	for word in sampleMap:
		if sampleMap[word] != samplePassage.FreqOf(word):
			passed = False
			break
	print(testMsg(passed))
except:
	print("\nError detected. Recheck your function") 




