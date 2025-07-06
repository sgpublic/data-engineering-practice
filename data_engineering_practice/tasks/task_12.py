"""
# 2.2.t12 实验任务 12

指导书要求编写代码使用 NumPy 中的 random、array、arange 函数。

指导书中使用了 numpy.mat() 函数，现已被 numpy.asmatrix() 替代。
"""
import numpy
from numpy import random

from data_engineering_practice.utils.logging import new_logger


logger = new_logger("task-12")

if __name__ == '__main__':
    logger.info("--- random ---")
    logger.info("随机 2 个随机数。")
    result = random.random(size=2)
    logger.info(f"结果：{result}")
    logger.info("随机一个 3x2 的数组，数值范围在 [-5, 0)。")
    result = 5 * random.random((3, 2)) - 5
    logger.info(f"结果：{result}")
    logger.info("--- random ---")

    logger.info("--- array ---")
    logger.info("创建 1x3 的数组。")
    result = numpy.array([1, 2, 3])
    logger.info(f"结果：{result}")
    logger.info("--- array ---")

    logger.info("--- asmatrix ---")
    logger.info("使用数组创建 2x2 的矩阵。")
    result = numpy.asmatrix([[1, 2], [3, 4]])
    logger.info(f"结果：\n{result}")
    logger.info("使用字符串创建 2x2 的矩阵。")
    result = numpy.asmatrix("1, 2; 3, 4")
    logger.info(f"结果：\n{result}")
    logger.info("--- asmatrix ---")

    logger.info("--- arange ---")
    logger.info("创建 1 ~ 3（不包括 3）的数组")
    result = numpy.arange(1, 3)
    logger.info(f"结果：{result}")
    logger.info("创建 2 ~ 10（不包括 10）、步长为 2 的数组")
    result = numpy.arange(2, 10, 2)
    logger.info(f"结果：{result}")
    logger.info("--- arange ---")
