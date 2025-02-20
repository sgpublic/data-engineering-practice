"""
# 1.1.t1 实验任务 1

指导书推荐使用 Anaconda，理由是手动安装需要的依赖库繁琐且出错概率较高。

此处使用 poetry 自动管理依赖解决问题，虽然创建项目时仍需要手动添加依赖，但使用 poetry 可避免依赖冲突等问题，且不受限于 Python 版本。

```shell
poetry add numpy pandas scikit_learn
```
"""
from data_engineering_practice.utils.deps_version import print_dep_version
from data_engineering_practice.utils.logging import new_logger

logger = new_logger("task-01")


def main():
    print_dep_version(logger, "numpy")
    print_dep_version(logger, "pandas")
    print_dep_version(logger, "scikit-learn")
