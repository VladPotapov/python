def dividend(num):
    return num - ((num / 100) * 13)

agro = 225.38
polymetal = dividend(65.87)
novatek = dividend(23.74)
nlmk = dividend(7.25 * 10)
sber = dividend(18.7 * 20)
gazprom = dividend(7 * 70)
dividends = int(agro + polymetal + novatek + nlmk + sber + gazprom)

print(dividends)