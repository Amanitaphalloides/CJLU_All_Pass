def longest_word(s):
    words = s.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

s = "A startup backed by the Japanese automaker has developed a test model that engineers hope will eventually develop into a tiny car with a driver who'll be able to light the Olympic torch in the 2020 Tokyo games."
result = longest_word(s)
print("最长的英文单词是：", result)
