# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os


class Spider0908Pipeline(object):  # 需要在setting.py里设置'coolscrapy.piplines.CoolscrapyPipeline':300
    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/bilibili.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['title'] + ' ')
            f.write(item['upname'] + '\n')
        return item