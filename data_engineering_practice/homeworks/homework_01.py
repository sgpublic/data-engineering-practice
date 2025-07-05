"""
# 1.h1 课后作业（一）

指导书要求输出 “Hello Python!” 并验证 XGBoost 和 LightGBM 安装成功。
"""

from data_engineering_practice.utils.logging import new_logger

logger = new_logger("homework-01")


if __name__ == '__main__':
    # 验证 xgboost 安装
    try:
        import xgboost as xgb
        logger.info("xgboost 已成功安装")
    except ModuleNotFoundError:
        logger.error("xgboost 未成功安装")

    # 验证 lightgbm 安装
    try:
        import lightgbm as lgb
        logger.info("lightgbm 已成功安装")
    except ModuleNotFoundError:
        logger.error("lightgbm 未成功安装")

    # 输出 Hello Python!
    logger.info("Hello Python!")
