import os
import jieba

MAX_CUT = 10000
FILE_NAME = 'news_sohusite_cutword.txt'

def cut(done, total, lines, f):
    for index in range(done, total):
        f.writelines([' '.join(jieba.cut(lines[index])) + '\n'])
        print('切词完成：%.2f%% [%d/%d]' %((index + 1) * 100 / total, index + 1, total))

with open('news_sohusite_xml.dat', 'r', encoding='gb18030') as fi:
    lines = fi.readlines()

lines = list(map(lambda x: x[9:-11], filter(lambda x: x[:9] == '<content>', lines)))

total = len(lines)
if 'MAX_CUT' in vars() and total > vars()['MAX_CUT']:
	total = vars()['MAX_CUT']
done = 0

while done != total:
    try:
        if not os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'w', encoding='utf8') as fo:
                done = 0
                cut(done, total, lines, fo)
                done = total
        else:
            with open(FILE_NAME, 'r+', encoding='utf8') as fo:
                done = len(fo.readlines())
                cut(done, total, lines, fo)
                done = total
    except:
        pass
