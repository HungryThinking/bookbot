def number_of_words(string):
	words = string.split()
	num_words = len(words)
	return num_words

def characters_count(text: str) -> dict[str, int]:
	counts = {}
	for char in text.lower():
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	return counts

def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
	sorted_list = [
		{"char": char, "count": count}
		for char, count in char_counts.items()
		if char.isalpha()
	]
	sorted_list.sort(key=lambda x: x["count"], reverse=True)
	return sorted_list
