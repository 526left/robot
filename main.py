import sys
from pojo.robot import Robot

# 需要创建全局材料需求信息表
# 格式：   {"7"：{"produced": 1,
#               "工作台编号": 10,
#                   "4"   :  {"produced": 0,
#                               "1"     : 0,
#                               "2"     : 1},
#                   "5"   :  {"produced": 0,
#                               "1"     : 0,
#                               "3"     : 1},
#                   "6"   :  {"produced": 0,
#                               "2"     : 0,
#                               "3"     : 1},
#               }
#         }




def initialize():
    """
        初始化函数：
            功能：
                1. 初始化机器人信息（编号，位置）
                2. 初始化工作台信息（编号，位置）
                3. 初始化可供应对应材料的工作台信息
    :return:
    """
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = 49.75
    robot_dict = {}                                              # 保存机器人对象{编号：机器人对象}
    workbench_dict = {}                                          # 保存工作台对象{工作台编号： 工作台对象}
    workbench_article_dict = dict((i ,[]) for i in key)          # 保存材料对应工作对象{可获取材料编号：[工作台对象1， 工作台对象2]}
    print(workbench_article_dict)

    robot_define_id = 0                                          # 定义机器人编号id
    workbench_define_id = 0                                      # 定义工作台编号id

    # 循环读入输入知道输入为“OK” 停止
    while True:
        info = input()
        if info == "OK":
            break
        x = 0.25
        for i in info:
            if i == '.':
                x += 0.5
                continue
            elif i == 'A':
                robot = Robot()
                robot_dict[robot_define_id] = robot
                robot_define_id += 1
                continue
            else:
                workbench_article_id = eval(i)
                workbench = Workbench()
                workbench_dict[workbench_define_id] = workbench
                workbench_article_dict[workbench_article_id].append(workbench)
        y -= 0.5









if __name__ == "__main__":
    initialize()
    print("OK")
    sys.stdout.flush()

    try:
        while True:
            # 获取帧id 并且作为标准输入的第一行
            frame_id = input().split(' ')[0]
            print(frame_id)
            # 读取后面的内容并执行算法




    except EOFError:
        pass

















