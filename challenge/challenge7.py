
i = input("名前を入力してください。")
with open("st.txt", "w") as f:
    f.write(i)

with open("st.txt", "r") as f:
    print(f.read())

list1 = ["トップガン", "Risky Business", "Minority Report"]
list2 = ["Titanic", "The Revenant", "Inception"]
list3 = ["Training Day", "Men on Fire", "Flight"]

import csv
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))