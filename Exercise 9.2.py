# Exercise 2
# Write a function called has_no_e that returns True if the given word doesn’t have
# the letter “e” in it.

# Modify your program from the previous section to print only the words that have
# no “e” and compute the percentage of the words in the list that have no “e”.

def has_no_e_one():
    fin = open(r"C:\\Users\wicke\Downloads\Hello.txt")
    for line in fin:
        if line.find("e") == -1:
            return("True")


def has_no_e():
    fin = open(r"C:\\Users\wicke\Downloads\Hello.txt")
    number_of_words = 0
    count = 0
    for line in fin:
        number_of_words = number_of_words + 1
        words = line.strip()
        if words.find("e") == -1:
            print(words)
            count = count + 1
    percent_of_words = (count/number_of_words) * 100
    print("Percent:", percent_of_words)
