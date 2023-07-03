# -*- coding: utf-8 -*-
'''
	递归出当前目录下的所有子文件（夹），并重新重组为可读的形式

'''
## comment

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QWidget
from tkinter import filedialog 
import sys, os
import os.path
from file_tree_ui import Ui_File_tree


class FileWidget(QWidget):
    '''GUI主界面，ui文件由Ui_File_trees设置'''

    def __init__(self) -> None:
        super(FileWidget, self).__init__()
        self.ui = Ui_File_tree() #实例化UI
        self.ui.setupUi(self)
        self.cur_root = filedialog.askdirectory(initialdir='D:/') 
        # self.cur_root = 'D:/HC11_Images_20230309'
        self.ex = [self.cur_root] #用于记录导出内容

        self.ui.treeWidget.setColumnCount(1)
        self.ui.treeWidget.setHeaderLabel('PathView')
        self.tree_root = QTreeWidgetItem(self.ui.treeWidget)
        self.tree_root.setText(0, self.cur_root)
        self.dic_root = {self.cur_root:self.tree_root}  #root tree 的字典

        self.ui.pushButton.clicked.connect(self.reload_tree)    #绑定刷新按键
        self.ui.pushButton_2.setCheckable(False)    #默认不可点击导出按键
        self.ui.pushButton_2.clicked.connect(self.export_tree)    #绑定刷新按键


    def tree_builder(self, upper_path:str, dic_tree:dict, mark:int) -> dict:
        '''生成Qtree视图
        p:upper_path-文件/文件夹真实路径, 
            dic_tree-上级tree的字典{上一级文件夹路径：上一级文件夹的Qtree对象}
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
                cname = '[ '+ cname +' ]' #标记文件夹，用于区分
                self.ex.append('├{} {}\n'.format("─"*mark, cname))   #记录文件夹，用于导出
            elif not os.path.isdir(true_path):
                self.ex.append('├{} {}\n'.format("─"*mark, cname))  #记录文件，用于导出
            child_tree = QTreeWidgetItem(dic_tree[upper_path])  #这里实现了文件和文件夹的tree——adding
            child_tree.setText(0, cname)
            dic_tree[upper_path].addChild(child_tree)

            if os.path.isdir(true_path):
                dict_lower_tree[true_path] = child_tree
                self.tree_builder(true_path, dict_lower_tree, mark+1)

        self.ui.pushButton_2.setCheckable(True)     #激活导出按键
        
    def run_all(self):
        self.tree_builder(self.cur_root, self.dic_root, 0)  
        self.ui.treeWidget.expandAll()    

    def reload_tree(self):
        '''清空原来的tree，重新加载'''
        self.ui.treeWidget.clear()
        self.tree_root = QTreeWidgetItem(self.ui.treeWidget)
        self.tree_root.setText(0, self.cur_root)
        self.dic_root = {self.cur_root:self.tree_root}  #root tree 的字典
        self.tree_builder(self.cur_root, self.dic_root)   
        self.ui.treeWidget.expandAll()

    def export_tree(self):
        '''导出文件目录结构'''

        # 新建txt，以上一级文件夹名命名
        w_file = open('FileTree.txt', 'w', encoding='utf-8')
 
        for e in self.ex:
            w_file.write(e)
            # 写入当前文件路径
        w_file.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Files = FileWidget()

    Files.run_all()

    Files.show()
    app.exec_()

