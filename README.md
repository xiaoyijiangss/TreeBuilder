# Dir.Tree.Builder
### Based on PYQT5 to creat a Qtree view to show all the sub-files and sub-folders for a folder.  
### Tested in Windows 10.  
### Download the *file_tree_ui.py* with *app_file_tree.py* file together and run the _app_file_tree_ scipt.
### use *requirements.txt* to install the package imported by the scripts:
```cmd
pip install -r requirements.txt
# if in china , use this:
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/  
```
If you click the "export" button, a txt file will created in the woring path named "FileTree.txt".  


For those who are reluctant to use the _PyQT_, just dowload the _app_file_lister.py and run, it will creat a txt file in your current path named "FileTree.txt".   

## Example output
```txt
D:/Program Files (x86)
┆︎ ── Qt Designer
┆︎      ┆︎── bearer
┆︎      ┆︎     ┆︎── qgenericbearer.dll
┆︎      ┆︎── canbus
┆︎      ┆︎     ┆︎── qtpassthrucanbus.dll
┆︎      ┆︎     ┆︎── qtpeakcanbus.dll
┆︎      ┆︎     ┆︎── qtsysteccanbus.dll
┆︎      ┆︎     ┆︎── qttinycanbus.dll
┆︎      ┆︎     ┆︎── qtvectorcanbus.dll
┆︎      ┆︎── iconengines
┆︎      ┆︎     ┆︎── qsvgicon.dll
┆︎      ┆︎── imageformats
┆︎      ┆︎     ┆︎── qgif.dll
┆︎      ┆︎     ┆︎── qicns.dll
┆︎      ┆︎     ┆︎── qico.dll
┆︎      ┆︎     ┆︎── qjpeg.dll
┆︎      ┆︎     ┆︎── qsvg.dll
┆︎      ┆︎     ┆︎── qtga.dll
┆︎      ┆︎     ┆︎── qtiff.dll
┆︎      ┆︎     ┆︎── qwbmp.dll
┆︎      ┆︎     ┆︎── qwebp.dll
```