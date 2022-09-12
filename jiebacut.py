import jieba

fR = open('douban.txt','r') #读取文件
sent = fR.read()
sent_list = jieba.cut(sent) #使用jieba进行分词
fW = open('douban2.txt','w',encoding='utf-8') #写入文件
fW.write(' '.join(sent_list))
fR.close()
fW.close()
