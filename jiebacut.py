import jieba

fR = open('bilibili.txt','r') #读取文件
sent = fR.read()
sent_list = jieba.cut(sent) #使用jieba进行分词
fW = open('bilibili_cut.txt','w',encoding='utf-8') #写入文件
fW.write(' '.join(sent_list))
fR.close()
fW.close()
