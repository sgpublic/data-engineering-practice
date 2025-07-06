"""
# 2.h2 课后作业（二）

要求如下：

1、用 Python 实现 F1-score，并自己构建一个简易数据集进行测试。

2、用 Python 中的 for 循环、列表推导式，分别实现计算：1+2+3+...+1000。

3、随机生成一个五列十行的 Dataframe 的数据类型，行列索引自定义，绘制出对应的柱状图、散点图，以及在查询官网学习绘制一个课程未讲解（即除柱状图、饼图、散点图、箱线图以外的图形）的数据分析图形。

官方文档链接：`Official-Doc`_

.. _Official-Doc: https://pandas.pydata.org/pandas-docs/version/0.23/api.html#api-dataframe-plotting
"""
import numpy
import pandas
import os

from data_engineering_practice.utils.logging import new_logger

logger = new_logger("homework-02")


def f1_score() -> float:
    """
    计算 F1-score。
    随机生成一个 int 类型的数组，长度为 500，范围 [0, 1000]，假定 [0, 500) 为反例，[500, 1000] 为正例。
    现模拟一个二分类器，将 [0, 300)U(800, 1000] 预测为反例，[300, 800] 预测为正例。
    理论上此二分类器的 F1-score 应为 0.6。
    :return: F1-score
    """
    dataset = numpy.random.randint(low=0, high=1001, size=500)
    logger.info(f"随机生成数据集：\n{dataset}")
    tp = len([x for x in dataset if 500 <= x <= 800])
    logger.info(f"真正例：{tp}")
    fp = len([x for x in dataset if 300 <= x < 500])
    logger.info(f"假正例：{fp}")
    tn = len([x for x in dataset if 0 <= x < 300])
    logger.info(f"真反例：{tn}")
    fn = len([x for x in dataset if 800 < x <= 1000])
    logger.info(f"假反例：{fn}")
    result = 2 * tp / (2 * tp + fp + fn)
    logger.info(f"F1-score：{result}")
    return result

def sum_for() -> int:
    """
    用 for 循环实现计算 1+2+3+...+1000
    :return: 1+2+3+...+1000
    """
    logger.info("用 for 循环实现计算 1+2+3+...+1000")
    result = 0
    for i in range(1, 1001):
        result += i
    logger.info(f"结果：{result}")
    return result

def sum_list_comprehension() -> int:
    """
    用列表推导式实现计算 1+2+3+...+1000
    :return: 1+2+3+...+1000
    """
    logger.info("用列表推导式实现计算 1+2+3+...+1000")
    result = sum(i for i in range(1, 1001))
    logger.info(f"结果：{result}")
    return result

def chart_area(base_path: str):
    data = pandas.DataFrame({'x': numpy.arange(10), 'y': numpy.random.rand(10)})
    logger.info(f"使用数据：\n{data}\n生成区域图")
    chart = data.plot.area(x='x', y='y')
    save_path = f'{base_path}/area.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_bar(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(10, 4), columns=[x for x in 'abcd'])
    logger.info(f"使用数据：\n{data}\n生成柱状图")
    chart = data.plot.bar()
    save_path = f'{base_path}/bar.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_barh(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(10, 4), columns=[x for x in 'abcd'])
    logger.info(f"使用数据：\n{data}\n生成水平柱状图")
    chart = data.plot.barh()
    save_path = f'{base_path}/barh.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_box(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(10, 5), columns=[x for x in 'abcde'])
    logger.info(f"使用数据：\n{data}\n生成箱线图")
    chart = data.plot.box()
    save_path = f'{base_path}/box.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_density_kde(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(10, 2), columns=['x', 'y'])
    logger.info(f"使用数据：\n{data}\n生成核密度图")
    chart = data.plot.density()
    save_path = f'{base_path}/density.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_hexbin(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(1000, 2), columns=['x', 'y'])
    logger.info(f"使用数据：\n{data}\n六边形分箱图")
    chart = data.plot.hexbin(x='x', y='y', gridsize=20)
    save_path = f'{base_path}/hexbin.jpg'
    chart.get_figure().savefig(save_path)
    logger.info(f"保存图片至 {save_path}")

def chart_hist(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(10, 2), columns=['a', 'b'])
    logger.info(f"使用数据：\n{data}\n生成直方图")
    chart = data.plot.hist()
    save_path = f'{base_path}/hist.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_line(base_path: str):
    data = pandas.DataFrame({'x': numpy.arange(20), 'y': numpy.random.rand(20)})
    logger.info(f"使用数据：\n{data}\n生成折线图")
    chart = data.plot.line(x='x', y='y')
    save_path = f'{base_path}/line.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

def chart_scatter(base_path: str):
    data = pandas.DataFrame(numpy.random.rand(50, 2), columns=['x', 'y'])
    logger.info(f"使用数据：\n{data}\n生成散点图")
    chart = data.plot.scatter(x='x', y='y')
    save_path = f'{base_path}/scatter.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

if __name__ == '__main__':
    logger.debug("--- F1-score ---")
    f1_score()
    logger.debug("--- F1-score ---")

    logger.debug("--- sum for ---")
    sum_for()
    logger.debug("--- sum for ---")

    logger.debug("--- sum list comprehension ---")
    sum_list_comprehension()
    logger.debug("--- sum list comprehension ---")

    logger.debug("--- chart bar ---")
    base_path = './outputs/homework-02'
    logger.info(f"创建文件夹 {base_path} 以存放输出图片...")
    os.makedirs(base_path, exist_ok=True)
    chart_area(base_path)
    chart_bar(base_path)
    chart_barh(base_path)
    chart_box(base_path)
    chart_density_kde(base_path)
    chart_hexbin(base_path)
    chart_hist(base_path)
    chart_line(base_path)
    chart_scatter(base_path)
    logger.debug("--- chart bar ---")
