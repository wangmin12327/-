class Student:
    """
    学生类：对学生学号、姓名、年龄、性别等个人信息数据处理
          类属性：student;
          构造方法：__init__();
          实例方法：add_stu() ; alter_stu(); del_stu_by_sid(); del_stu_by_name()
    """
    # 类属性，student,学生个人信息存放字典
    #       stu_list,学生个人信息存放列表
    #       del_stu_list,待删除的学生个人信息存放列表
    #       sid_list,学生学号信息存放列表
    #       name_list,已添加学生姓名信息存放列表
    student = {}
    stu_list = []
    del_stu_list = []
    sid_list = []
    name_list = []

    def __init__(self, sid=None, name=None, age=None, sex=None):
        """
        初始化学生个人信息
        :param sid: 学生学号;
        :param name: 学生姓名;
        :param age: 学生年龄;
        :param sex: 学生性别;
        """
        self.sid = sid
        self.name = name
        self.age = age
        self.sex = sex

    def add_stu(self):
        """
        添加新学生信息：函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
        :return: 返回是否添加成功的结果;
        """
        while self.sid in Student.sid_list:
            self.sid = input("学号不可重复,添加失败,请重新输入学号：")
        Student.student = {"sid": self.sid, "name": self.name, "age": self.age, "sex": self.sex}
        Student.stu_list.append(Student.student)
        Student.sid_list.append(self.sid)
        Student.name_list.append(self.name)
        print("添加成功!")
        return Student.stu_list

    def alter_stu(self):
        """
        修改学生信息：通过学号修改学生信息，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
        :return:如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功;
        """
        while self.sid not in Student.sid_list:
            self.sid = input("学生不存在,修改失败,请重新输入学号：")
        for stu in Student.stu_list:
            if stu["sid"] == self.sid:
                stu["name"] = self.name
                stu["age"] = self.age
                stu["sex"] = self.sex
                print("修改成功!")
        return Student.stu_list

    def del_by_sid(self):
        """
        通过学号删除学生信息：通过学号删除学生信息，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
        :return: 如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功;
        """
        while self.sid not in Student.sid_list:
            self.sid = input("学生不存在,删除失败,请重新输入学号：")
        for stu in reversed(Student.stu_list):
            if stu["sid"] == self.sid:
                Student.stu_list.remove(stu)
                Student.sid_list.remove(self.sid)
        print("删除成功!")
        return Student.stu_list

    def del_by_name(self):
        """
        通过姓名删除学生信息：参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
        :return: 如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功;
        """
        while self.name not in Student.name_list:
            self.name = input("学生不存在,删除失败,请重新输入姓名：")
        Student.del_stu_list = [stu for stu in Student.stu_list if stu["name"] == self.name]
        for stu in reversed(Student.del_stu_list):
            if stu["name"] in Student.name_list:
                Student.name_list.remove(self.name)
            if stu["sid"] in Student.sid_list:
                Student.sid_list.remove(stu["sid"])
            Student.stu_list.remove(stu)
        print("删除成功!")
        return Student.stu_list

    def sear_by_sid(self):
        """
        通过学号查询学生信息：参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
        :return: 如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功;
        """
        while self.sid not in Student.sid_list:
            self.sid = input("学生不存在,查询失败,请重新输入学号：")
        sear_stu_list = [stu for stu in Student.stu_list if stu["sid"] == self.sid]
        print("查询成功!")
        return sear_stu_list

    def sear_by_name(self):
        """
        通过姓名查询学生信息：参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否查询成功
        :return: 如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否查询成功;
        """
        while self.name not in Student.name_list:
            self.name = input("学生不存在,查询失败,请重新输入姓名：")
        Student.stu_list = [stu for stu in Student.stu_list if stu["name"] == self.name]
        print("查询成功!")
        return Student.stu_list


class Print:
    """
    打印类：打印学生信息列表
         构造方法：__init__();
         实例方法：print_all_stu();
    """

    def __init__(self, all_stu_list):
        """
        初始化打印所有学生信息列表
        :param all_stu_list: 所有学生信息列表;
        """
        self.all_stu_list = all_stu_list

    def print_all_stu(self):
        """
        打印所有学生信息列表
        :return: 返回所有学生信息列表;
        """
        for stu_ele in self.all_stu_list:
            str_stu = f"学号：{stu_ele['sid']}\n姓名：{stu_ele['name']}\n年龄：{stu_ele['age']}\n性别：\
{stu_ele['sex']}\n\n"
            print(str_stu)


def menu():
    """
    菜单
    :return:返回用户输入的编号
    """
    print("****************************************")
    print("*                                学生管理系统*")
    print("*              1. 添加新学生信息              *")
    print("*              2. 通过学号修改学生信息*")
    print("*              3. 通过学号删除学生信息*")
    print("*              4. 通过姓名删除学生信息*")
    print("*              5. 通过学号查询学生信息*")
    print("*              6. 通过姓名查询学生信息*")
    print("*              7. 显示所有学生信息*")
    print("*              8. 退出系统*")
    print("****************************************")
    select_op = input("输入编号选择操作：")
    return select_op


def control(select_op):
    """
    控制函数：用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
    :param select_op: 输入编号
    :return: 返回菜单的输出
    """
    if select_op == '1':
        sid = input("请输入新学生学号：")
        name = input("请输入新学生姓名：")
        age = input("请输入新学生年龄：")
        sex = input("请输入新学生性别：")
        stu = Student(sid, name, age, sex)
        stu_info_list = stu.add_stu()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '2':
        sid = input("请输入待修改的学生学号：")
        name = input("请输入修改后学生姓名：")
        age = input("请输入待修改后学生年龄：")
        sex = input("请输入待修改后学生性别：")
        stu = Student(sid, name, age, sex)
        stu_info_list = stu.alter_stu()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '3':
        del_sid = input("请输入待删除的学生学号：")
        stu = Student(del_sid)
        stu_info_list = stu.del_by_sid()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '4':
        del_name = input("请输入待删除的学生姓名：")
        stu = Student(None, del_name)
        stu_info_list = stu.del_by_name()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '5':
        sear_sid = input("请输入待查询的学生学号：")
        stu = Student(sear_sid)
        stu_info_list = stu.sear_by_sid()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '6':
        sear_name = input("请输入待查询的学生姓名：")
        stu = Student(None, sear_name)
        stu_info_list = stu.sear_by_name()
        print_stu_info = Print(stu_info_list)
        print_stu_info.print_all_stu()

    elif select_op == '7':
        print_stu_info = Print(Student.stu_list)
        print_stu_info.print_all_stu()

    elif select_op == '8':
        stu_list_str = '\n'.join(map(str, Student.stu_list))
        rel_stu_file = open(r"data/data_stu.txt", "w")
        rel_stu_file.write(stu_list_str)
        rel_stu_file.close()

        sid_list_str = '\n'.join(map(str, Student.sid_list))
        rel_sid_file = open(r"data/data_sid.txt", "w")
        rel_sid_file.write(sid_list_str)
        rel_sid_file.close()

        name_list_str = '\n'.join(map(str, Student.name_list))
        rel_name_file = open(r"data/data_name.txt", "w")
        rel_name_file.write(name_list_str)
        rel_name_file.close()
        exit()


if __name__ == '__main__':
    # 定义空字典student，用于接收单个学生个人信息
    student = {}

    # 定义空列表，用于接收多条学生个人信息记录
    init_stu_list = []

    # 定义学号空列表，用于判断添加学生信息时，学号是否重复；用于判断修改学生信息时，学号是否存在；用于判断查询学生信息时，学号是否存在；
    init_sid_list = []

    # 定义姓名空列表，用于判断修改学生信息时，姓名是否存在；用于判断查询学生信息时，姓名是否存在；
    init_name_list = []

    # 程序启动时从文件加载数据到程序

    file_stu = open(r"data/data_stu.txt", "r")
    content_stu = file_stu.read()
    if content_stu:
        Student.stu_list = content_stu.split('\n')
        Student.stu_list = [eval(item) for item in Student.stu_list]
        print(Student.stu_list)
    file_stu.close()

    file_sid = open(r"data/data_sid.txt", "r")
    content_sid = file_sid.read()
    if content_sid:
        Student.sid_list = content_sid.split('\n')
        print(Student.sid_list)
    file_sid.close()

    file_name = open(r"data/data_name.txt", "r")
    content_name = file_name.read()
    if content_name:
        Student.name_list = content_name.split('\n')
        print(Student.name_list)
    file_name.close()

    SELECT_OP = ['1', '2', '3', '4', '5', '6', '7', '8']
    op = '1'
    while op in SELECT_OP:
        op = menu()
        control(select_op=op)
