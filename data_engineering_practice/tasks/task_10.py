"""
# 2.2.t10 实验任务 10

指导书要求编写代码使用列表推导式。
"""
from data_engineering_practice.utils.logging import new_logger


logger = new_logger("task-00")

if __name__ == '__main__':
    logger.info("生成一个 1 ~ 10 的列表")
    list1: list = list(range(1, 11))
    logger.info(f"结果：{list1}")
    logger.info("生成一个列表，元素为 1 ~ 10 的平方")
    list2: list = [x * x for x in list1]
    logger.info(f"结果：{list2}")
    logger.info("生成一个列表，元素为 1 ~ 10 中偶数的平方")
    list2: list = [x * x for x in list1 if x % 2 == 0]
    logger.info(f"结果：{list2}")
    logger.info("同时遍历两个字符串中的字符，并进行排列组合")
    list2: list = [m + n for m in 'ABC' for n in 'XYZ']
    logger.info(f"结果：{list2}")
