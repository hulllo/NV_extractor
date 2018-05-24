import os
import re
import logging
def main():
    path = "./source"
    files= os.listdir(path)
    nvidlist = []
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            f = open(path+"/"+file,encoding = 'utf-8'); #打开文件
            iter_f = iter(f); #创建迭代器
            try:
                for line in iter_f:
                    try:
                        nvid = re.findall(r'<NvItem id="(\d+)"', line)[0]
                        nvidlist.append(nvid)
                    except IndexError as e:
                        logging.warn(e, line)
            except UnicodeDecodeError as e:
                logging.error('UnicodeDecodeError:{0}'.format(file))
                input()

    return(nvidlist)

if __name__ == '__main__':
    main()
