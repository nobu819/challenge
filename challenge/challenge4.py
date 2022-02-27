z = "カミュ"
print(z[0])
print(z[1])
print(z[2])

a = input("どんなもの？")
b = input("誰に？")
c = "私は昨日、{}を撮って、{}に送った。".format(a,b)
print(c)

e = "aldous Huxley was born in 1894.".upper()
print(e)

print("いつ？ どこで？ 誰が？".split(" "))

words = ("The", "Fox", "jumped", "over", "the", "fence", ".")
print(" ".join(words[0:5]),"".join(words[5:7]))

print("A screaming comes across the sky.".replace("s","$"))

print("Hemingway".index("m"))

print("みるみるうちに黒い雲が集まっていく'キュムロニンバス!'師匠が唱えると、辺りは嵐とかした。")

print("three"+" three"+" three")
print("three "*3)

f = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(f[:10])