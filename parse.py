import re

with open("./console-export-clean.txt") as f:
    i = 1
    for line in f.readlines():
        items = line.split("\t")
        title = items[1]
        link = items[2]
        print(f"{i}: {title=}, {link=}")
        i += 1
