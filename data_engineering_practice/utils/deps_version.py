from importlib import metadata
from importlib.metadata import PackageNotFoundError
from logging import Logger


def print_dep_version(logger: Logger, dep_name: str):
    try:
        version = metadata.version(dep_name)
        logger.info(f"已安装依赖 {dep_name}=={version}")
    except PackageNotFoundError:
        logger.error(f"依赖 {dep_name} 未安装！")
