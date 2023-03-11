import sys
from pojo.robot import Robot

class robot:
    def __init__(self,
                 id,
                 coord_x,
                 coord_y,
                 forward,
                 angular_v =0,
                 linear_v=0,
                 radius=0.45,
                 mass=9):
        self.id = id                            # 机器人id
        self.coord_x = coord_x                  # 机器人x坐标
        self.coord_y = coord_y                  # 机器人y坐标
        self.forward = forward                  # 机器人朝向
        self.angular_v = angular_v              # 机器人角速度
        self.linear_v = linear_v                # 机器人线速度
        self.radius = radius                    # 机器人半径
        self.mass = mass                        # 机器人质量 单位/kg



def initialize():
    y = 49.75
    robot_dict = {}
    workbench_dict = {}
    robot_define_id = 1
    while True:
        info = input()
        if info == "OK":
            break
        x = 0.25
        for i in info:
            if i == '.':
                x += 0.25
                continue
            elif i == 'A':
                robot = Robot()
                robot_dict[robot_define_id] = robot
                robot_define_id += 1
                continue
            else:
                workbench_id = eval(i)
                workbench = Workbench()
                workbench_dict[workbench_id] = workbench










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

















