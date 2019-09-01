#!/sur/bin/python
# -*-coding:utf-8-*-
import yaml
with  open(file="1.yaml",mode="r",encoding="utf-8")  as f:
    a = yaml.load(f,Loader=yaml.FullLoader)
    print(a)
