import os
def 压缩包炸弹生成方法(文件路径:str, 文件数量:int, 文件大小:int):
    if not os.path.exists(文件路径):
        os.mkdir(文件路径)
    os.chdir(文件路径)

    for i in range(文件数量):
        字节 = i.to_bytes(2, 'little')
        with open('{}.txt'。format(str(i)), 'wb') as f:
            f.seek(文件大小 - 1)
            f.write(字节)

文件大小 = 1073741824  # 单位为字节   1048576为1MB     1073741824   为1GB
压缩包炸弹生成方法(文件路径=r'C:\Users\zjh\Desktop', 文件数量=3, 文件大小=文件大小)
