from stats import words_counter, count_characters, sorted_list
import sys
# returns the contents of a file into a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    chars=count_characters(get_book_text(sys.argv[1]))
    result = sorted_list(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    words_counter(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    for i in range(0,len(result)):
        temp = result[i]
        if temp["char"].isalpha() == False:
            continue
        print(f"{temp["char"]}: {temp["num"]}")
    print("============= END ===============")

main()
