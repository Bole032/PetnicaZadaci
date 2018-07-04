# -*- coding: utf-8 -*-
import numpy as np
import math
import pandas as pd
import matplotlib as plt

products = pd.read_csv("products.csv")
print(products)

orders = pd.read_csv("orders.csv")
print(orders)

br_proizvoda = products.count()["product_id"]
br_narudzbina = orders.count()["order_id"]
br_korisnika = orders["user_id"].drop_duplicates().count()
print(br_proizvoda)
print(br_narudzbina)
print(br_korisnika)

