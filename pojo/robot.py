


class Robot:
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
        self.nearest_workbench = {}






