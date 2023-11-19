from es import init_connection, WordEs


def load_words():
    with open("words.txt", 'r') as f:
        lines = f.readlines()
        _count = 10000
        for line in lines:
            _count -= 1
            if _count == 0:
                break
            WordEs(word=line.strip()).save()


if __name__ == '__main__':
    init_connection()
    load_words()
