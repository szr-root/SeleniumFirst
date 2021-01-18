from SeleniumSecond.Page.mainpage import MainPage


class TestAddDepartmemt:
    def setup_class(self):
        # 实例化 MainPage类
        self.main = MainPage()

    def test_addmember(self):
        #1. 首页跳转到通讯录页面 2. 添加部门 3. 获取部门信息
        result = self.main.goto_adddepartment_page().add_department().get_department_list()
        assert "坑钱部" in result

    def test_add_member_fail(self):
        #1. 首页跳转到通讯录页面 2. 添加部门 3. 获取部门信息
        toast = self.main.goto_adddepartment_page().add_department_fail().get_toast()
        assert toast == "该部门已存在"
