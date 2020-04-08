from efficient_apriori import apriori
import csv

director = '宁浩'
file_name = './' + director + '.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
# 加载数据
data = []
for names in lists:
    name_new = []
    for name in names:
        # 去掉演员数据中的空格
        name_new.append(name.strip())
    data.append(name_new[1:])
data = [tuple(i) for i in data if i != []]
# 挖掘频繁项集和关联规则
itemsets, rules = apriori(data, min_support=0.35, min_confidence=1)
print(itemsets)
print(rules)
