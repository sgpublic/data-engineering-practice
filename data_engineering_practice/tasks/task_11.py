"""
# 2.2.t11 实验任务 11

指导书要求编写代码使用 Lambda 表达式。

PS：由于 Lambda 内容不能包含复杂表达式，个人认为使用 lambda 不如使用 def 定义函数。
"""
from data_engineering_practice.utils.logging import new_logger


logger = new_logger("task-11")

if __name__ == '__main__':
    logger.info("创建 Lambda 表达式：my_lambda = lambda x: x + 1")
    my_lambda = lambda x: x + 1
    logger.info(f"结果：{my_lambda}")
    logger.info("调用 Lambda 表达式：my_lambda(5)")
    result = my_lambda(5)
    logger.info(f"结果：{result}")
