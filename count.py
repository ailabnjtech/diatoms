# 统计文件夹下的图片个数
import os
path = './datasets/test'  # 父文件夹路径
all_folds = os.listdir(path)   # 解析出父文件夹中所有的文件名称，并以列表的格式输出，
# 例如['add','common-mobile-web-app-icons.zip', '新建 Microsoft Word 文档.docx', 'arrow_down']
l = []
for i in range(len(all_folds)):
    fold_path = os.path.join(path,all_folds[i])  # 将父文件夹路径加上子文件的名称，例如：'D:/testin/common-mobile-web-app-icons/add'
    if os.path.isdir(fold_path):   # 判断该文件是否为文件夹
        count_fold = len(os.listdir(fold_path))
        # print(all_folds[i],count_fold)
        l.append((all_folds[i],count_fold))  # 得到列表，列表里面是数组，数组里面是文件名称和该文件名称文件夹中图片个数
# print(l)
dic_file = dict(l)  # 数组转成字典
# dic_file
txt_file = os.getcwd()+'\count.txt'  # os.getcwd()得到当前路径，并在当前路径下建一个txt文本文件
out = open(txt_file,'w')  # 打开文本文件
for i in  dic_file:  # 循环字典的键
    out.write(i)  # 写入键，既文件夹名称
    # out.write(': ')
    # out.write(str(dic_file[i]))  # 写入值，既文件夹名称下的图片个数
    out.write('\n')  # 换行
out.close()  # 关闭txt文本文件

# 统计有多少个文件夹
# import os
# all_folds = os.listdir('./datasets/test')
# all_folds = [x for x in all_folds if '.' not in x]
# print(len(all_folds))
# all_folds[:5]



