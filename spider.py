import socket

import requests
import socks
from lxml import etree

from dlSite import DlSite


class Spider:
    def __init__(self, url: str, proxy_url="127.0.0.1", port=11223):
        """

        :param url: DlSite链接
        :param proxy_url: 代理服务器地址
        :param port: 代理服务器端口
        """
        self.port = port
        self.proxy_url = proxy_url
        self.url = url

    def get_html(self):
        """
        使用requests模块获取DlSite页面
        :return: resp
        """
        socks.set_default_proxy(socks.SOCKS5, self.proxy_url, self.port)
        socket.socket = socks.socksocket
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/65.0.3325.181 "
                          "Safari/537.36 "
        }
        return requests.get(self.url, headers=headers)

    def get_media(self):
        """
        解析resp 利用xpath获取DlSite的相关信息
        :return:
        """
        # 解析requests传回来的html
        html_data = etree.HTML(self.get_html().text)
        try:
            title = html_data.xpath("//h1[@id='work_name']/a/text()")[0]
            datetime = html_data.xpath("//table[@id='work_outline']//th[text()='贩卖日']//following-sibling::td//text()")[
                0]
            import time
            # 将获取到的年月日转换为 - 连接
            split_time = time.strptime(datetime, "%Y年%m月%d日")
            # {}-{:0>2d}-{:0>2d} 月份天数补零
            time = "{}-{:0>2d}-{:0>2d}".format(split_time.tm_year, split_time.tm_mon, split_time.tm_mday)
            work_type = html_data.xpath("//table[@id='work_outline']//div[@id='category_type']//span/text()")[0]
            age = html_data.xpath("//table[@id='work_outline']//div[@class='work_genre']//span/text()")[0]
            community = html_data.xpath("//span[@class='maker_name']/a/text()")[0]
            return DlSite(title, time, work_type, age, community)
        except BaseException:
            return None
