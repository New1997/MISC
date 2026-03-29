import re

# 1. Load the words into a list
# For Mac/Linux, use "/usr/share/dict/words"
# For Windows, replace with the path to your downloaded txt file
dict_path = "/usr/share/dict/words"

with open(dict_path, "r") as f:
    words = [word.strip() for word in f]

# 2. Define your Regex
# Example: Find 5-letter words starting with 'b' and ending with 'y'
play_again = True
while play_again:
    w_len=int(input("Number of characters of your word : "))
    to_ignore = ["" for i in range(w_len)]
    pattern = r"."*w_len
    orange_letters="etasnoihrdlcumwfgypbvkjxqz"[:w_len]#initialization to get first word
    found = False
    first_iter = True

    while not found:
        interim_pattern = ""
        for i in range(w_len):
            if pattern[i]=="." and to_ignore[i] != "":
                interim_pattern += r"[^"+to_ignore[i]+r"]"
            else:
                interim_pattern += pattern[i]
        interim_pattern = r"^"+interim_pattern+r"$"
        #print(interim_pattern)
        # 3. Filter the list
        matches = [w for w in words if re.search(interim_pattern, w, re.IGNORECASE)]
        if orange_letters:
            for i in orange_letters:
                interim_matches = [w for w in matches if re.search(i, w, re.IGNORECASE)]
                if interim_matches : # safegaurd for first word sugestion to not be empty
                    matches = interim_matches

        if first_iter:
            orange_letters=""
            first_iter=False
        for i in matches:
            print(i)
        validation = input("Has the solution been found ? [Y/y/1]/[N/n/0/anything else] : ")
        if validation in"Yy1":
            found = True
            play_again = input("Play again ? [Y/y/1]/[N/n/0/anything else] : ") in "Yy1"
        else:
            global_ignore = input("Grey letters (all at once) : ")
            for i in range(w_len):
                to_ignore[i] += global_ignore
            orange_len = int(input("Number of new orange letters : "))
            for i in range(orange_len):
                new_o_letter = input("Enter one orange letter : ")
                new_o_position = int(input("Enter the position of this orange character (1-"+str(w_len)+") : "))
                if new_o_letter not in orange_letters:
                    orange_letters += new_o_letter
                to_ignore[new_o_position-1] += new_o_letter
            green_len = int(input("Number of new green letters : "))
            for i in range(green_len):
                new_g_letter = input("Enter one green letter : ")
                new_g_position = int(input("Enter the position of this green character (1-"+str(w_len)+") : "))
                pattern=pattern[:new_g_position-1]+new_g_letter+pattern[new_g_position:]
