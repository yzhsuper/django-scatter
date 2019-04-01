# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import hashlib
import hmac


def md5_order_nubmer(order_number):
    """
    订单号加密
    :param order_number:
    :return:
    """
    encode_str = '%s_%s' % (order_number, 'KmPERPWELKNV')
    args = hashlib.md5(encode_str)
    return args.hexdigest()


def md5str(s):
    """
    md5加密
    :param s 需要加密的字符串:
    :return: 加密
    """
    args = hashlib.md5(s)
    return args.hexdigest()


def sha256(encrypt_str):
    """
    sha256加密
    :param encrypt_str:
    :return:
    """
    sh = hashlib.sha256(encrypt_str.encode('utf-8'))
    # print(encrypt_str)
    # args = sh.update(encrypt_str.encode())
    #
    # j = hmac.new(encrypt_str.encode('utf-8'), digestmod=hashlib.sha256)
    # print(j.digest())
    return sh.hexdigest()
