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

class StudentManagementSystem:
    """学生信息管理系统"""
    def __init__(self):
        self.students = {}
    
    def add_student(self):
        """添加学生"""
        print("\n--- 添加学生信息 ---")
        student_id = input("请输入学号: ")
        
        if student_id in self.students:
            print("该学号已存在！")
            return
        
        name = input("请输入姓名: ")
        age = input("请输入年龄: ")
        grade = input("请输入成绩: ")
        
        self.students[student_id] = Student(student_id, name, age, grade)
        print(f"学生 {name} 添加成功！")
    
    def view_all_students(self):
        """查看所有学生"""
        print("\n--- 所有学生信息 ---")
        if not self.students:
            print("暂无学生信息")
            return
        
        for student in self.students.values():
            student.display_info()
    
    def search_student(self):
        """查询学生"""
        print("\n--- 查询学生信息 ---")
        student_id = input("请输入要查询的学号: ")
        
        if student_id in self.students:
            self.students[student_id].display_info()
        else:
            print("未找到该学生！")
    
    def delete_student(self):
        """删除学生"""
        print("\n--- 删除学生信息 ---")
        student_id = input("请输入要删除的学号: ")
        
        if student_id in self.students:
            name = self.students[student_id].name
            del self.students[student_id]
            print(f"学生 {name} 删除成功！")
        else:
            print("未找到该学生！")
    
    def display_statistics(self):
        """显示统计信息"""
        if not self.students:
            print("暂无学生信息")
            return
        
        total = len(self.students)
        grades = [float(s.grade) for s in self.students.values() if s.grade.replace('.', '').isdigit()]
        
        if grades:
            average = sum(grades) / len(grades)
            max_grade = max(grades)
            min_grade = min(grades)
            
            print(f"\n--- 统计信息 ---")
            print(f"学生总数: {total}")
            print(f"平均成绩: {average:.2f}")
            print(f"最高成绩: {max_grade}")
            print(f"最低成绩: {min_grade}")
    
    def run(self):
        """运行系统"""
        while True:
            print("\n" + "=" * 40)
            print("学生信息管理系统")
            print("=" * 40)
            print("1. 添加学生")
            print("2. 查看所有学生")
            print("3. 查询学生")
            print("4. 删除学生")
            print("5. 统计信息")
            print("6. 退出系统")
            print("=" * 40)
            
            choice = input("请选择操作 (1-6): ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                print("感谢使用学生信息管理系统！")
                break
            else:
                print("无效选择，请重新输入！")

# 演示如何使用文件操作
def file_operations_demo():
    """文件操作示例"""
    print("\n--- 文件操作示例 ---")
    
    # 写入文件
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write("这是第一行内容\n")
        f.write("这是第二行内容\n")
        f.write("Python文件操作示例\n")
    
    print("文件写入完成")
    
    # 读取文件
    with open('sample.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("\n文件内容：")
        print(content)
    
    # 追加内容
    with open('sample.txt', 'a', encoding='utf-8') as f:
        f.write("这是追加的内容\n")

# 主程序
if __name__ == "__main__":
    # 运行学生管理系统
    system = StudentManagementSystem()
    system.run()
    
    # 运行文件操作示例
    # file_operations_demo()
    
    # 列表推导式示例
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"\n偶数列表: {even_numbers}")
    
    # 字典推导式示例
    squares = {x: x**2 for x in range(1, 6)}
    print(f"数字平方字典: {squares}")
