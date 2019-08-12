import matplotlib.pyplot as plt
import seaborn as sns
spam_data["label"].value_counts().plot(kind = 'pie', explode = [0, 0.1], figsize = (6, 6), autopct = '%1.1f%%', shadow = True)
plt.ylabel("Positif vs Negatif")
plt.legend(["positif", "negatif"])
plt.show()
