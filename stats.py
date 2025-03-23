def get_book_content(book_path):
    with open(book_path, encoding="utf8") as f:
        file_contents = f.read()
        return file_contents


def get_num_words(content) -> int:
    return len(content.split())


def get_num_chars(content: str):
    res = {}

    for chars in content.lower():
        if chars not in res.keys():
            res[chars] = 1
        else:
            res[chars] += 1

    return res


def show_stats(book_path):
    content = get_book_content(book_path)
    num_words = get_num_words(content)
    num_chars = get_num_chars(content)
    show_num_words(num_words)
    show_num_chars(num_chars)


def show_num_words(num_words):
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


def show_num_chars(num_chars):
    print("--------- Character Count -------")
    for k in dict(
        sorted(num_chars.items(), key=lambda item: item[1], reverse=True)
    ).keys():
        if k.isalpha():
            print(f"{k}: {num_chars[k]}")
