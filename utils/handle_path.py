from email import utils
import os


# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 工具方法路径
utils_path = os.path.join(project_path, 'utils')

# startproject 生成的网站路径
mysite_path = os.path.join(project_path, 'mysite')

