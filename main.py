
#10-misol
n = 1

def ikkilantir():
    global n
    n = n * 2

for i in range(4):
    ikkilantir()

print(n)


#11-misol
count = 0

def oshir():
    global count
    count += 1

def nolga_qaytarish():
    count = 0

oshir()
oshir()
oshir()
nolga_qaytarish()
print(count)


#12-misol
soni = 5

def checker():
    if soni > 3:
        natija = "katta"
    else:
        natija = "kichik"
    print(natija)

checker()
soni = 2
checker()


#13-misol
limit = 3
chaqiruvlar = 0

def bajar():
    global chaqiruvlar
    if chaqiruvlar < limit:
        chaqiruvlar += 1
        print(f"Bajarildi: {chaqiruvlar}")
    else:
        print("Limit tugadi")

for _ in range(5):
    bajar()
#

#14-misol
   x = 10


    def f():
        x += 5
        print(x)


    f()
