import os
from keras.models import load_model
import  numpy as np
model = load_model('save_model.keras')

model.summary()

os.chdir('./notFall')

with open('0.txt', 'r') as file:
    lines = file.readlines()
xRealtime = []
for line in lines:
    elements = [float(x) for x in line.strip().split(',')]
    xRealtime.extend(elements)
xRealtime = xRealtime[:230]

xRealtime = np.array(xRealtime).reshape(1, -1)  # Assuming xRealtime is 1 sample

predictions = model.predict(xRealtime)

class_labels = (predictions > 0.5).astype(int)

print(class_labels)
