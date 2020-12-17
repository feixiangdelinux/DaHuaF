def read_ispose(pash):
    """读取配置文件

    :param int pash: json文件路径.
    """
    f = open(pash, 'r', encoding="utf-8")
    return f.read()


class DisposeUtil:
    """大话西游配置文件的工具类
    包含读取配置文件，写入配置文件，json文件转换等功能
    """
