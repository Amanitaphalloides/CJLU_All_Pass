def find_longest_words(filename, num_words=5):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()

        words = [word.strip() for word in words]

        words.sort(key=len, reverse=True)

        longest_words = words[:num_words]

        return longest_words

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []


if __name__ == "__main__":
    filename = 'words.txt'
    longest_words = find_longest_words(filename)
    print("最长的五个单词是:")
    for word in longest_words:
        print(word)
