import pandas as pd
import numpy as np
import sys  

spam_data = pd.read_csv('/resources/data/datalaguSaya.csv')
spam_data['label'] = np.where(spam_data['label']=='positif',1,0)
print(spam_data.shape)
spam_data.head(10)

import matplotlib.pyplot as plt
import seaborn as sns
spam_data["label"].value_counts().plot(kind = 'pie', explode = [0, 0.1], figsize = (6, 6), autopct = '%1.1f%%', shadow = True)
plt.ylabel("Positif vs Negatif")
plt.legend(["positif", "negatif"])
plt.show()
