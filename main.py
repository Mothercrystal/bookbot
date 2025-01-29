def main ():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()


    words = file_contents.split()
    print(len(words))


    letters = file_contents.lower()


    lower_case_dict = {}
    for i in letters:
        if not i.isalpha():
            continue
        if i not in lower_case_dict:
            lower_case_dict[i] = 1
        else:
            lower_case_dict[i] += 1   

    

    def sort_on(lower_case_dict):
        return lower_case_dict["num"]

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")
    reading_time = calculate_reading_time(len(words))
    print(reading_time + "\n")

    char_list = []
    for char, count in lower_case_dict.items():
        char_dict = {"letter" : char, "num" : count}
        char_list.append(char_dict)

    char_list.sort(key=sort_on, reverse=True)

    for char_info in char_list:
        print(f"The '{char_info["letter"]}' was found {char_info["num"]} times")

    print("--- End report ---")


def calculate_reading_time(word_count, reading_speed=238):    
    reading_time = word_count / reading_speed
    hours = int((reading_time) / 60)
    minutes = int((reading_time) - (hours * 60))
    seconds = int((reading_time - int(reading_time)) * 60)
    return f"Reading time: {hours} hours, {minutes} minutes and {seconds} seconds"
    


if __name__ == "__main__":
    main()

