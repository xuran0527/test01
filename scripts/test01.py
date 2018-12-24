import allure

class Test_report:
    @allure.step("测试第一步")
    def test_a(self):
        print("aaa")
        assert 1

    @allure.step("测试第二步")
    def test_b(self):
        print("bbb")
        allure.attach("提示1","bbb")
        print("hello")
        allure.attach("提示2", "hello")
        assert 0