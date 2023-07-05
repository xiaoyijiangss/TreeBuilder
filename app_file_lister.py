# -*- coding: utf-8 -*-
'''
	create a txt with to show you sub folders' and sub files' information

'''

from tkinter import filedialog 
import os
import os.path

class Parser():
    '''GUI主界面，ui文件由Ui_File_trees设置'''

    def __init__(self) -> None:
        
        self.cur_root = filedialog.askdirectory(initialdir='D:/') 
        # self.cur_root = 'D:/HC11_Images_20230309'
        self.ex = [self.cur_root + '\n'] #用于记录导出内容


    def path_builder(self, upper_path:str, mark:int) -> dict:
        '''生成Qtree视图
        p:upper_path-文件/文件夹真实路径, 
            mark:用于缩进计数
        r:dict-{当前文件夹路径：当前文件夹的Qtree对象}
        '''
        dict_lower_tree = {}
        lower_pathes_middle = os.listdir(upper_path)
        lower_pathes = sorted(lower_pathes_middle, key=lambda \
        x: os.path.isdir(os.path.join(upper_path, x)), reverse=True)  #排序，文件夹在前，文件在后
               
        for e_path in lower_pathes:
            true_path = os.path.join(upper_path, e_path)    #真实路径，用于判断是否需要递归
            cname = os.path.split(e_path)[-1]   #tree中显示的名称，取路径/文件的最后一级
            if os.path.isdir(true_path):
                # cname = cname + '>>' #标记文件夹，用于区分
                self.ex.append('┆︎ {}{}\n'.format("     ┆︎"*mark, "── "+cname))   #记录文件夹，用于导出
            elif not os.path.isdir(true_path):
                self.ex.append('┆︎ {}{}\n'.format("     ┆︎"*mark, "── "+cname))  #记录文件，用于导出

            if os.path.isdir(true_path):
                self.path_builder(true_path, mark+1)

    def export_tree(self):
        '''导出文件目录结构'''

        # 新建txt，以上一级文件夹名命名
        file_name = os.path.split(self.cur_root)[-1]
        w_file = open(file_name + '.txt', 'w', encoding='utf-8')
 
        for e in self.ex:
            w_file.write(e)
            # 写入当前文件路径
        w_file.close()
        cur_dir = os.getcwd() + r'\\' + file_name + '.txt'
        print('{} created'.format(cur_dir))

    def run_all(self):
        self.path_builder(self.cur_root, 0)  
        self.export_tree()

if __name__ == '__main__':
    Pathlister = Parser()
    Pathlister.run_all()


