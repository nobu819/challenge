a = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for i in a:
    print(i)

for i in range(25, 26):
    print(i)

for i, new in enumerate(a):
    i = str(i)
    print(i+","+new)

i = 0
print("数字当てゲーム!")
while True:
    print("数字を入力するか、qで終了します。")
    j =input("1~100の中で入力してください。")
    if j == "q":
        break
    j = int(j)
    k = (i+j)
    if k == 55:
        print("正解!")
        break
    else:
        print("不正解")

list1 = [8, 19, 148, 4]
list2 = [9,  1, 33, 83]
added = []

for i in list1:
    for j in list2:
        added.append(i*j)
print(added)