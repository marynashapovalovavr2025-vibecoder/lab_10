import matplotlib.pyplot as plt
f = open('файл.txt', 'rt')
vowels = "aeuioy"
L = f.readlines()
freq ={}
for line in L:
    for char in line:
        if char.lower() in vowels:
            ch_lower = char.lower()
            freq[ch_lower] = freq.get(ch_lower, 0) + 1
f.close()
letters = freq.keys()
values = freq.values()
plt.bar(letters, values, label = "Кількість літер", color='green')
plt.xlabel('Голосні літери')
plt.ylabel('Частота')
plt.legend()
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()
plt.close()
print(f"Гістограму збережено у файл {'histogram.png'}")