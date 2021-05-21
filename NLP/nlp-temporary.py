# from snownlp import SnowNLP
# s = SnowNLP(u'这个东西真心很赞')
# print(s.words)

import snownlp as nlp
# s = nlp.SnowNLP(u'这个东西真心很赞')
# print(s.words)
# print(s.tags)
print('请输入评价：')
comment = input()
while comment != 'Q':
    s = nlp.SnowNLP(comment)
    # 中文自然语言中积极情绪的概率
    positive_prob = s.sentiments
    print(s.sentiments)
    if positive_prob > 0.7:
        print('持积极评价')
    elif positive_prob > 0.3:
        print('中性评价')
    else:
        print('持消极评价')

    print('请输入评价：')
    comment = input()
