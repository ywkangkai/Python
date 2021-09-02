import shutil


# 拷贝文件
# shutil.copy2('原文件', '现文件')
# shutil.copy2('file', 'temp')

# 拷贝目录
# shutil.copytree("原目录", "新目录", ignore=shutil.ignore_patterns("*.pyc"))

#ignore表示可指定忽略哪些文件不拷贝
# shutil.copytree("目标路径", "新路径", ignore=shutil.ignore_patterns("__init__.py"))

# 删除目录
# shutil.rmtree("temp", ignore_errors=True)
# shutil.rmtree("路径", ignore_errors=True) #ignore_errors=True表示强删，如某些文件正在开启中也能删掉

# 移动文件/目录
# shutil.move("目标路径", "新路径", copy_function=shutil.copy2)

# 获取磁盘使用空间
# total, used, free = shutil.disk_usage(".")
# print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB"%(total / 1073741824, used / 1073741824, free / 1073741824))
#
# 压缩文件
# shutil.make_archive('压缩文件夹的名字', 'zip','待压缩的文件夹路径') #第二个参数表示压缩格式
# shutil.make_archive('logging2', 'zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/随机数')

# 解压文件
# shutil.unpack_archive('zip文件的路径.zip'，'解压到目的文件夹路径')
# shutil.unpack_archive('/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/logging2.zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/tmp')