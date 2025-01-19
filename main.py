def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        #print(file_contents)
        print(f"{len(file_contents.split())} words found in the document")
        characters = {}
        lowered = file_contents.lower()
        for char in lowered:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
        #print(characters)
        report_list = []
        for alpha in characters:
            if alpha.isalpha():
                alphadic = {}
                alphadic["letter"] = alpha
                alphadic["num"] = characters[alpha]
                report_list.append(alphadic)
        report_list.sort(reverse = True, key = sort_on)
        for info in report_list:
            print(f"The '{info['letter']}' character was found {info['num']} times")

def sort_on(report_list):
    return report_list["num"]

main()