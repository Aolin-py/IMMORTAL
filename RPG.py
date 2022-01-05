import time
from variable import *
import def_
import os
import threading
import datetime


#
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
#
#  .............................................
#           佛祖保佑             永无BUG
#
def start(name):
    print(name)
    while True:
        def_.cedn()


print(fun)
# def_.menpai_list_out('e')
print('版本version-5w-2d1a\033[1;33m')
time.sleep(0.3)
print('{==============}')
time.sleep(0.3)
def_.poem_w(poem, 2)
time.sleep(0.2)
print('{==============}')
time.sleep(0.3)
print('\033[0m欢迎来到' + '\033[1;34m' + ' 道 途 ' + '\033[0m')
time.sleep(0.7)
print('输入/help查看操作指南')
print('\033[2;31m先/save再下线！\033[0m')
account = def_.Archive(name, password)
if os.path.exists('UserConfig.config'):
    account.read_Archive()
else:
    pass
account = def_.Archive(name, password)
account.judgment()
def_.update_announcement()
weather_t = threading.Thread(target=def_.weather, args=(1,))
# music_p = threading.Thread(target=music,args=('',))
game_start = threading.Thread(target=start, args=('',))
auto_save = threading.Thread(target=account.save_Archive, args=('', ))

weather_t.start()
# music_p.start()
game_start.start()

print('现在是' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
