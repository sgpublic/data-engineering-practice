"""
# 1.t3 实验任务 3

指导书要求手动下载 lightgbm 的预编译 whl 文件并安装，此处使用 pixi 直接安装。

```shell
pixi add --pypi lightgbm
```
"""
from data_engineering_practice.utils.deps_version import print_dep_version
from data_engineering_practice.utils.logging import new_logger

logger = new_logger("task-03")


if __name__ == '__main__':
    print_dep_version(logger, "lightgbm")
