# ---- dictionary 기본 구성 & 조회 ----

people = {'korean': 380, 'american': 42, 'japanese': 15}

# ---- 중첩 dictionary 구조 ----​
chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}

chnInfos['하트시그널2']['hit'] += 3000
# print(chnInfos['하트시그널2']['hit'])

newchn = '아는형님'
newhit = 350000
newlike = 8800

# chnInfos[newchn]['hit'] = newhit  빈 딕셔너리에에 키 값을 추가 할 수 없다

chnInfos[newchn] = {'hit':newhit, 'like':newlike}
# print(chnInfos)

# for chnInfos in chnInfos.keys():
#     print(chnInfos)

# for chnInfos in chnInfos.values():
#     print(chnInfos)

for chnInfos in chnInfos.items():
    print(chnInfos)



# chnInfos['하트시그널2']['score'] = 88
# print(chnInfos['하트시그널2']['score'])
#
