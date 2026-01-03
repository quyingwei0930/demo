"""
学生信息管理系统 - 样例代码
功能：添加、查看、查询、删除学生信息
"""

class Student:
    """学生类"""
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        """显示学生信息"""
        print(f"学号: {self.student_id}")
        print(f"姓名: {self.name}")
        print(f"年龄: {self.age}")
        print(f"成绩: {self.grade}")
        print("-" * 30)

    
    # 字典推导式示例
    squares = {x: x**2 for x in range(1, 6)}
    print(f"数字平方字典: {squares}")

