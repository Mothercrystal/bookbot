def main ():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()


    words = file_contents.split()
    print(len(words))


    letters = file_contents.lower()
    #print(letters)

    lower_case_dict = {}
    for i in letters:
        if not i.isalpha():
            continue

        if i not in lower_case_dict:
            lower_case_dict[i] = 1

        else:
            lower_case_dict[i] += 1   

    print(lower_case_dict)
            

if __name__ == "__main__":
    main()

