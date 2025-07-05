"""
# 1.t1 实验任务 1

指导书推荐使用 Anaconda，理由是手动安装需要的依赖库繁琐且出错概率较高。

此处使用 pixi 自动管理依赖解决问题，虽然创建项目时仍需要手动添加依赖，但使用 pixi 可避免依赖冲突等问题，甚至可以用它来安装 Python。

```shell
pixi add --pypi numpy pandas scikit_learn
```
"""
from data_engineering_practice.utils.deps_version import print_dep_version
from data_engineering_practice.utils.logging import new_logger

logger = new_logger("task-01")


if __name__ == '__main__':
    print_dep_version(logger, "numpy")
    print_dep_version(logger, "pandas")
    print_dep_version(logger, "scikit-learn")
