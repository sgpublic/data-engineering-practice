"""
# 1.1.t2 实验任务 2

指导书要求手动下载 xgboost 的预编译 whl 文件并安装，此处使用 poetry 直接安装。

```shell
poetry add xgboost
```
"""
from data_engineering_practice.utils.deps_version import print_dep_version
from data_engineering_practice.utils.logging import new_logger

logger = new_logger("task-02")


if __name__ == '__main__':
    print_dep_version(logger, "xgboost")
