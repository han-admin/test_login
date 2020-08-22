# -*- coding: utf-8 -*-
import allure


class TestContact:

    @allure.severity('normal')
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach('输入用户名','测试输入了用户名：hello, 1')
        print("输入账号")

        allure.attach('输入密码','测试输入了密码：123, 1')
        print('输入密码')

        allure.attach('登录', '点击登录')
        print('点击登录')
        assert 1

    @allure.severity('critical')
    @allure.step(title="输入账号")
    def test_name(self):
        print("123")
        assert 1

    @allure.severity('blocker')
    @allure.step(title="输入密码")
    def test_pass(self):
        print("123")
        assert 1
