from stats import show_stats
import sys


def main():
    book = sys.argv[1]
    print_banner(book)
    show_stats(book)
    print_end_banner()


def print_banner(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")


def print_end_banner():
    print("============= END ===============")


if __name__ == "__main__":
    main()

