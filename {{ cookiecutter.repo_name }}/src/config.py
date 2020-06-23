import os


class DIR:
    ROOT = os.path.join(os.path.dirname(__file__), os.path.pardir)
    #example of config usage
    yolomodelpath = os.path.join(
        os.path.dirname(__file__), "data/yolovr_cpu_nms.pb"
    )


