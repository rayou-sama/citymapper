f = open("network_walk.csv", 'r')
next(f)
for line in f:
    items = line.rstrip("\n").split(";")
    print(f"INSERT INTO walk VALUES ( \'{items[0]}\'", end='')
    for item in items[1:] :
        item = item.replace("'", "''")
        print(f", \'{item}\'", end='')
    print(", '0');")
