import os.path
import re
import sys

from spider import Spider


def get_rj_code(filename):
    """
    根据文件名获取rj号
    :param filename: 文件名
    :return: rj号
    """
    return re.search(r'RJ\d{6}', filename).group(0)


def rename(url, filename):
    spider = Spider(url)
    media = spider.get_media()
    if media is not None:
        suffix = os.path.splitext(filename)[-1]
        real_name = "({}) [{}][{}][{}] {}" \
            .format(media.work_type, media.datetime, rj_code, media.community, media.title)
        name = real_name + suffix
        name = re.sub(r'[\\/:*?"<>|]', '-', name)  # 去掉非法字符
        print(' \033[1;35m {} \033[0m'.format(name))
        return name
    else:
        return None


if __name__ == '__main__':
    file = sys.argv[1]
    # path = ['F:\收藏\DLSite\汉化']
    # 如果是文件夹 则遍历文件夹下的文件
    if os.path.isdir(file):
        for filename in os.listdir(file):
            rj_code = get_rj_code(filename)
            url = "https://www.dlsite.com/maniax/work/=/product_id/" + rj_code + ".html/?locale=zh_CN"
            name = rename(url, filename)
            if name is not None:
                os.rename(file + "\\" + filename, file + "\\" + name)
            else:
                print("\033[31m{}\033[0m".format(filename))
    # 如果是文件 则直接修改文件名
    else:
        # 文件名
        filename_no_path = os.path.basename(file)
        rj_code = get_rj_code(filename_no_path)
        path = os.path.realpath(file)
        url = "https://www.dlsite.com/maniax/work/=/product_id/" + rj_code + ".html/?locale=zh_CN"
        name = rename(url, filename_no_path)
        if name is not None:
            os.rename(file, path + "\\" + name)
        else:
            print("\033[31m{}\033[0m".format(file))
