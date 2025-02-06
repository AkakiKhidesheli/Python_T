a = 5  # =   მინიჭება

b = 7
b += 5  # ახალი b=ძველი b+5

c = 10
c -= 2  # c=c-2

d = 5
d *= 2  # d=d*2
print(d)

e = 4
e /= 4  # e=e/4
print(e)

f = 10
f %= 4  # f=f%4
print(f)

g = 17
g //= 5  # g=g%5
print(g)

h = 10
h **= 2  # h=h**2
print(h)

a1 = 6
a2 = 6
c1 = a1 > a2
c2 = a1 < a2
print(c1)
print(c2)
print(a1 == a2)

# = არის მინიჭება, == არის შედარება (ტოლია თუ არა)

################
# and, or, not
################
a3 = 10
a4 = 6
b3 = 7
b4 = 8
print(a3 > a4 and b3 > b4)  # True and False     ერთ-ერთი თუა არასწორი, ბეჭდავს არასწორს
print(a3 > a4 or b3 > b4)  # True or False      ერთ-ერთი თუა სწორი, ბეჭდავს სწორს
print(not a3 > a4)  # მოქმედებს, როგორც უარყოფა
print(a3 > a4 and (not b3 > b4))

f11 = 6
f12 = 7
print(f11 is f12)
print(f12 is not f11)

a123 = 'Sakartvelo'
print('a' in a123)  # არის თუ არა ცვლადში
print('k' not in a123)
print('s' in a123)
print('q' in a123)

# ! ნიშნავს არას
# != ნიშნავს არ უდრის

cvladi1 = 6904
cvladi2 = 3884

if cvladi1 < cvladi2:  # პირველი პირობა
    print("cvladi1 < cvladi2")
    print('Finished')
elif cvladi1 == cvladi2:  # მეორე პირობის შემოწმება, თუ პირველი მართალი არაა
    print("cvladi1 == cvladi2")
else:  # მოქმედებს, თუ არცერთი if და elif არ სრულდება
    cvladi1 += 5
    # print("cvladi1 > cvladi2")

if 'a' in 'Sakartvelo':
    if 'l' in 'Sakartvelo':
        if 'b' in 'Sakartvelo':
            print('b is in Sakartvelo')
        else:
            print('b is not in Sakartvelo')
    else:
        print('l is not in Sakartvelo')

# Ctrl alt l      -git push -u origin main გასწორებაgit init