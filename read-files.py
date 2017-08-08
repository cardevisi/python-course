file = open("text-for-read.txt")

all_card_list = []

for line in file:
    line = line.strip()
    line = line
    print(line)
    all_card_list.append(line)

print(all_card_list)

file.close()