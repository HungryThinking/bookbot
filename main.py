from stats import number_of_words
from stats import characters_count
from stats import sort_char_counts
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def print_report(filepath: str, char_counts: dict[str, int], word_count: int):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    sorted_counts = sort_char_counts(char_counts)
    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	word_count = number_of_words(book_text)
	char_count = characters_count(book_text)
	print_report(filepath, char_count, word_count)

main()
