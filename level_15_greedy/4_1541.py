mathExpr = input()
# mathExpr = "1+2-3-4-5"

negIdx = mathExpr.find("-")
if negIdx < 0:
    posNum = sum(list(map(int, mathExpr.replace("+", " ").split())))
    print(posNum)
else:
    posNum = sum(list(map(int, mathExpr[:negIdx].replace("+", " ").split())))
    negNum = sum(list(map(int, mathExpr[negIdx+1:].replace("+", "-").replace("-", " ").split())))
    print(posNum - negNum)
