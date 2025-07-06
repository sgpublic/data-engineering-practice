"""
# 2.2.t13 实验任务 13

指导书要求编写代码使用 Pandas 中的 Dataframe、Series 等类型。
"""
import pandas
from numpy import random

from data_engineering_practice.utils.logging import new_logger


logger = new_logger("task-13")

if __name__ == '__main__':
    logger.info("--- Series ---")
    index1 = ['b', 'c', 'd', 'e']
    logger.info(f"创建索引为 {index1} 的 Series")
    result1 = pandas.Series(random.random(len(index1)), index1)
    logger.info(f"结果：\n{result1}")
    my_dict = { 'a': random.random(), 'b': random.random(), 'c': random.random() }
    logger.info(f"将 dict（{my_dict}）转为 Series")
    result2 = pandas.Series(my_dict)
    logger.info(f"结果：\n{result2}")

    logger.info("--- DataFrame ---")
    logger.info("使用上述两个 Series 组成一个两列的 DataFrame")
    result = pandas.DataFrame({
        'result1': result1,
        'result2': result2,
    })
    logger.info(f"结果：\n{result}")
    index2 = result.index
    logger.info(f"查看行索引：{index2}")
    index3 = result.columns
    logger.info(f"查看列索引：{index3}")
    logger.info("--- DataFrame ---")
