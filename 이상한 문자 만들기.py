def solution(s):
    words_list = s.split(" ")
    new_list = []

    for i in words_list:
        new_words = ""
        for j in range(len(i)):
            if j % 2 == 0:
                new_words += i[j].upper()
            else:
                new_words += i[j].lower()

        new_list.append(new_words)

    return " ".join(new_list)