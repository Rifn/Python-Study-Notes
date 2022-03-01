import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

f = open("text_file/santi.txt", "r", encoding="utf-8")
text = f.read()
x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)


wc = WordCloud(font_path=‪", background_color="white", repeat=True, mask=mask)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()