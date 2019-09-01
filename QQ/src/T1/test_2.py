#!/sur/bin/python
# -*-coding:utf-8-*-
from until.ReadDate import s
from time import sleep
from until.点击滑动 import swipe_left
from until.点击滑动 import swipe_right
from until.点击滑动 import swipe_up
from until.点击滑动 import swipe_down
import  pytest



def test_1(lian):
    swipe_right(lian)
    sleep(10)
    swipe_left(lian)
    sleep(10)
    swipe_up(lian)
    sleep(10)
    swipe_down(lian)
