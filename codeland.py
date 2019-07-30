def processLand(count, priceList, petrolAmountList):
    least = priceList[0]
    amt = 0
    for i in range(count):
        if priceList[i] < least:
            amt += priceList[i] * petrolAmountList[i]
            least = priceList[i]
        else:
            amt += least * petrolAmountList[i]
    print(amt)


total = int(input())

for i in range(total):
    pricePetrol = []
    petrolAmt = []
    count = int(input())
    data = input().strip()
    pricePetrol = list(map(int, data.split(" ")))
    data = input().strip()
    petrolAmt = list(map(int, data.split(" ")))
    print("pricePetrol", pricePetrol)
    print("petrolAmt", petrolAmt)
    processLand(count, pricePetrol, petrolAmt)
