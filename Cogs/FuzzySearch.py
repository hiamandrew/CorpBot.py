import difflib
from   operator    import itemgetter

def search(searchTerm, list, numMatches : int = 3, keyName : str = None):
	"""Searches the provided list for the searchTerm - using a keyName if provided for dicts."""
	if len(list) < 1:
		return None
	# Iterate through the list and create a list of items
	searchList = []
	for item in list:
		if keyName:
			testName = item[keyName]
		else:
			testName = item
		matchRatio = difflib.SequenceMatcher(None, searchTerm, testName).ratio()
		searchList.append({ 'Name' : testName, 'Ratio' : matchRatio })
	# sort the servers by population
	searchList = sorted(searchList, key=lambda x:int(x['Ratio']), reverse=True)
	if numMatches > len(searchList):
		# Less than three - let's just give what we've got
		numMatches = len(searchList)
	return searchList[:numMatches]