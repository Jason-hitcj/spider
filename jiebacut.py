import jieba

fR = open('data_9.csv','r',encoding='utf-8') #读取文件
sent = fR.read()
sent_list = jieba.cut(sent) #使用jieba进行分词
fW = open('data_1.txt','w',encoding='utf-8') #写入文件
fW.write(' '.join(sent_list))
fR.close()
fW.close()
