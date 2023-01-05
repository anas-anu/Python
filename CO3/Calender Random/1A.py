import random
l1=['ANAS','SHAHABAS','SALU SAILAN','CUPPIDIE','SHEFNA','SREELAKSHMI','KATHU','YAZIM']
print(random.choices(l1))
print(random.choices(l1,k=2))
random.shuffle(l1)
print(l1)
print(random.randrange(1,6))
