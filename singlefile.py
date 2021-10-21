import os.path
import re

from spider import Spider


def get_rj_code(filename):
    """
    根据文件名获取rj号
    :param filename: 文件名
    :return: rj号
    """
    return re.search(r'RJ\d{6}', filename).group(0)


def re_name(url, filename):
    spider = Spider(url)
    media = spider.get_media()
    suffix = os.path.splitext(filename)[-1]
    if media is not None:
        real_name = "({}) [{}][{}][{}] {}" \
            .format(media.work_type, media.datetime, rj_code, media.community, media.title)
        name = re.sub(r'[\\/:*?"<>|]', '-', real_name)  # 去掉非法字符
        print(' \033[1;35m {} \033[0m'.format(name))
        return name + suffix
    else:
        print("\033[31m{}\033[0m".format(filename))


if __name__ == '__main__':
    # file = sys.argv[1]
    file = r"D:\Downloads\RJ345631 [Sumikko Circle] 与身娇柔弱对你一心一意的未婚妻进行甜蜜播种爱爱 (CV 大山チロル) _ WAV.rar"
    # path = ['F:\收藏\DLSite\汉化']
    # 文件名
    print("\033[0;36m{}\033[0m".format(file))
    filename_no_path = os.path.basename(file)
    rj_code = get_rj_code(filename_no_path)
    path = os.path.dirname(file)
    url = "https://www.dlsite.com/maniax/work/=/product_id/" + rj_code + ".html/?locale=zh_CN"
    name = re_name(url, filename_no_path)
    if name is not None:
        os.rename(file, path + os.sep + name)
    else:
        print("\033[31m{}\033[0m".format(file))
