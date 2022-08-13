FILENAME = 'text.txt'


if __name__ == "__main__":
    allowed_options = "[read_last_10_lines/read_first_10_lines/read_all_file/find_longest_word/lines_number/exit/]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")

        if desision == "read_first_10_lines":
            with open("text.txt") as myfile:
                read_first=myfile.readlines()[3:14]
                print((read_first))

        elif desision == "read_first_10_lines":
            with open("text.txt") as myfile:
                read_first=myfile.readlines()[0:10]
                print((read_first))

        elif desision == "lines_number":
            count = len(open("text.txt").readlines())
            print(count)

        elif desision == "read_all_file":
            file = open ('text.txt', mode="r", encoding="utf-8")
            data = file.read()
            lines = data.split("\n")
            print(lines)

        elif desision == "find_longest_word":
            file = open ('text.txt', mode="r", encoding="utf-8")
            data = file.read()
            lines = data.split()
            c=0
            for i in range(len(lines)):
                if len(lines[i])>c:
                    c=len(lines[i])
                    word=lines[i]
                    print (word)

        elif desision == "exit":
            print("Exiting...")
            break