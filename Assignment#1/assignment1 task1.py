import itertools
transactionLog=[
    {'orderId':1001,'customerId':'cust_Ahmed','productId':'prod_10'},
    {'orderId':1001,'customerId':'cust_Ahmed','productId':'prod_12'},
    {'orderId':1002,'customerId':'cust_Bisma','productId':'prod_10'},
    {'orderId':1002,'customerId':'cust_Bisma','productId':'prod_15'},
    {'orderId':1003,'customerId':'cust_Ahmed','productId':'prod_15'},
    {'orderId':1004,'customerId':'cust_Faisal','productId':'prod_12'},
    {'orderId':1004,'customerId':'cust_Faisal','productId':'prod_10'},
]

productCatalog={
    'prod_10':'Wireless Mouse',
    'prod_12':'Keyboard',
    'prod_15':'USB-C Hub'
}

def processTransactions(transactionList):
    cust_prod={}
    for record in transactionList:
        cust=record['customerId']
        prod=record['productId']
        if cust not in cust_prod:
            cust_prod[cust]=set()
        cust_prod[cust].add(prod)
    return cust_prod


def findFrequentPairs(customerData):
    pair_counts={}
    for cust, prod_set in customerData.items():
        if len(prod_set)<2:
            continue
        for p1,p2 in itertools.combinations(prod_set,2):
            pair=tuple(sorted((p1,p2)))
            if pair in pair_counts:
                pair_counts[pair]+=1
            else:
                pair_counts[pair]=1
    return pair_counts            

def getRecommendations(targetProductId,frequentpairs):
    related={}
    for pair,count in frequentpairs.items():
        if pair[0]==targetProductId:
            if pair[1] not in related:
                related[pair[1]]=count
            else:
                related[pair[1]]+=count
        elif pair[1]==targetProductId:
            if pair[0] not in related:
                related[pair[0]]=count
            else:
                related[pair[0]]+=count
    return related


def generateReport(targetProductId,recommendations,catalog):
    print(f'Recommendationsfor:{catalog[targetProductId]}')
    if not recommendations:
        print("No related products")
        return
    sorted_rec=sorted(recommendations.items(),key=lambda x:x[1],reverse=True)

    product_ids,count=zip(*sorted(recommendations.items(),key=lambda x:x[1],reverse=True))
    product_names=[catalog[p] for p in product_ids]
    for i,(name,count) in enumerate(zip(product_names,count),start=1):
        print(f'{i}.{name}-{count}')

transactions=(processTransactions(transactionLog))
print("transformed Data:\n",transactions)
pairCount=findFrequentPairs(transactions)
print("Pairs:\n",pairCount)
recommendations=getRecommendations('prod_10',pairCount)
print("Recommendations:\n",recommendations)
generateReport('prod_10',recommendations,productCatalog)

