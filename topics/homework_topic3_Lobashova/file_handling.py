from pathlib import Path
# Task 1: Read the file and remove equal lines (if any).
file1_path = Path("../../topics/03_file_handling_and_regex/assets") / "file1.txt"
#adding duplicate
with file1_path.open("a") as file:
    file.write("Apple\n")

with file1_path.open("r") as file:
    content_list = file.readlines()
    print(content_list)

without_dup = []
[without_dup.append(x) for x in content_list if x not in without_dup]
print(without_dup)

with file1_path.open("w+") as file:
    for l in without_dup:
        file.write(l)
    print(file.read())

#Task 2: Print out all words with length of n-characters

with file1_path.open("r") as file:
    content_list = file.readlines()
    for l in content_list:
        if len(l) == 7:
            print(l)

#Task 3: Combine two files into a third file

file2_path = Path("../../topics/03_file_handling_and_regex/assets") / "file2.txt"
file3_path = Path("../../topics/homework_topic3_Lobashova") / "Merge.txt"

with file1_path.open("r") as file:
    content1 = file.read()

with file2_path.open("r") as file:
    content2 = file.read()

content3 = content1 + content2
with file3_path.open("w+") as file:
    file.write(content3)
    print(file.read()) #Why this line doesn't work if the same line 19 works???
