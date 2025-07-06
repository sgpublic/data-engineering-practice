"""
# 2.2.t13 实验任务 14

指导书要求编写代码使用 Pandas 中的 Plot 类，用于数据可视化分析。
"""
import numpy
import pandas
import os

from data_engineering_practice.utils.logging import new_logger


logger = new_logger("task-14")

if __name__ == '__main__':
    base_path = './outputs/task14'
    logger.info(f"创建文件夹 {base_path} 以存放输出图片...")
    os.makedirs(base_path, exist_ok=True)

    data = pandas.Series(3 * numpy.random.random(4), index=[x for x in 'abcd'], name='Pie Chart')
    logger.info(f"使用数据：\n{data}\n生成饼图")
    chart = data.plot.pie(figsize=(6, 6))
    save_path = f'{base_path}/pie.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

    data = pandas.DataFrame(numpy.random.rand(10, 4), columns=[x for x in 'abcd'])
    logger.info(f"使用数据：\n{data}\n生成柱状图")
    chart = data.plot.bar()
    save_path = f'{base_path}/bar.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

    data = pandas.DataFrame(numpy.random.rand(10, 5), columns=[x for x in 'ABCDE'])
    logger.info(f"使用数据：\n{data}\n生成箱线图")
    chart = data.plot.box()
    save_path = f'{base_path}/box.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)

    data = pandas.DataFrame(numpy.random.rand(50, 2), columns=['X', 'Y'])
    logger.info(f"使用数据：\n{data}\n生成散点图")
    chart = data.plot.scatter(x='X', y='Y')
    save_path = f'{base_path}/scatter.jpg'
    logger.info(f"保存图片至 {save_path}...")
    chart.get_figure().savefig(save_path)
