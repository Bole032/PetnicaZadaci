import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv('orders.csv')
br_narudz_po_koris = orders.groupby('user_id').count()['order_id']
print(br_narudz_po_koris.mean())

brpbn = br_narudz_po_koris.groupby("order_id").count()['eval_set']
plt.plot(brpbn)
plt.show()