import re

with open("./console-export-clean.txt") as f:
    i = 1
    for i, line in enumerate(f.readlines()):
        _, title, link, _ = line.split("\t")
        print(f"{i}: {title=}, {link=}")
        i += 1
