import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# छोटा सा डमी डेटा (मान लीजिए: अनुभव के साल -> सैलरी)
# X = Experience (Years), y = Salary (Thousands में)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([30, 45, 60, 75, 90])

# मॉडल ट्रेन करना
model = LinearRegression()
model.fit(X, y)

# मॉडल को 'model.pkl' नाम से सेव करना
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl successfully!")