# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
#template = {
#    "name": "Galileo",
#    "type": "local",
#    "path": "../Galileo"
#}
enable_jsdelivr = {
    "enabled": True,
    "repo": "mikamichael/Blog-With-GitHub-Boilerplate@gh-pages"
}

category_by_folder = True


# 站点设置
site_name = "外贸启航站"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "MIKA"
email = "359911923@qq.com"
author_homepage = "https://www.wangxfei.com"
description = "外贸路上，愿我们都不再孤单。"
key_words = ['外贸', '建站', '商务英语', '客户开发']
language = 'zh-CN'
#external_links = [
#    {
#        "name": "Maverick",
#        "url": "https://github.com/AlanDecode/Maverick",
#        "brief": "🏄‍ Go My Own Way."
#    },
#    {
#        "name": "三無計劃",
#        "url": "https://www.imalan.cn",
#        "brief": "熊猫小A的主页。"
#    }
#]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

#social_links = [
#    {
#        "name": "Twitter",
#        "url": "https://twitter.com/AlanDecode",
#        "icon": "gi gi-twitter"
#    },
#    {
#        "name": "GitHub",
#        "url": "https://github.com/AlanDecode",
#        "icon": "gi gi-github"
#    },
#    {
#        "name": "Weibo",
#        "url": "https://weibo.com/5245109677/",
#        "icon": "gi gi-weibo"
#    }
#]

'''
head_addon = r
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "83GyzkaMH5GXodOfhqRVDGKQ-MdYXbMMI",
    "appKey": "urhuXqrhn7tDHztB8hQTCqcK",
    "visitor": True,
    "recordIP": True
}
'''
<<<<<<< HEAD
=======

>>>>>>> 9232800285f838ea133b11911e19c1c1efc9ca4d
'''

footer_addon = ''

body_addon = ''
