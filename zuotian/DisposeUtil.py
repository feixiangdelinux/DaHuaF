def read_ispose(pash):
    """读取配置文件

    :param int pash: json文件路径.
    """
    f = open(pash, 'r', encoding="utf-8")
    return f.read()
