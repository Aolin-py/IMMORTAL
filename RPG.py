import time
import def_
import os
import threading
import datetime
import random
if os.path.exists('UserConfig.py'):
    from UserConfig import *
else:
    name = ''
    password = ''

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
fun = random.randint(0, 100)  # fun值随机化

poem_l = ['平明拂剑朝天去，薄暮垂鞭醉酒归。', '五陵年少金市东，银鞍白马度春风。', '感君恩重许君命，泰山一掷轻鸿毛。', '手中电曳倚天剑，直斩长鲸海水开。', '万里浮云卷碧山，青天中道流孤月。',
          '暂就东山赊月色，酣歌一夜送泉明。', '我醉欲眠卿且去，明朝有意抱琴来。', '一身转战三千里，一剑曾当百万师。', '弓背霞明剑照霜，秋风走马出咸阳。', '三尺青锋怀天下，一骑白马开吴疆。']
poem = random.choice(poem_l)

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
print('输入help查看操作指南')
print('\033[2;31m现已添加自动保存功能！autosave <秒数>即可自定义设置！\033[0m')
account = def_.Archive(name, password)
account.judgment()
account = def_.Archive(def_.name, def_.password)
def_.update_announcement()
weather_t = threading.Thread(target=def_.weather, args=(1,))
# music_p = threading.Thread(target=music,args=('',))
game_start = threading.Thread(target=start, args=('',))
auto_save = threading.Thread(target=account.auto_save, args=('',))

weather_t.start()
# music_p.start()
game_start.start()
auto_save.start()

print('现在是' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
