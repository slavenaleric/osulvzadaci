#Ucitajte dane podatke u obliku numpy polja data. Podijelite ih na ulazne podatke X i izlazne
#2
#podatke y. Podijelite podatke na skup za ucenje i skup za testiranje modela u omjeru 80:20. 
#Dodajte programski kod u skriptu pomocu kojeg možete odgovoriti na sljedeca pitanja: 
#a) Izgradite model logisticke regresije pomo cu scikit-learn biblioteke na temelju skupa podataka za ucenje. 
#b) Provedite klasifikaciju skupa podataka za testiranje pomocu izgra denog modela logisticke 
#regresije.
#c) Izracunajte i prikažite matricu zabune na testnim podacima. Komentirajte dobivene rezultate.
#d) Izracunajte tocnost, preciznost i odziv na skupu podataka za testiranje. Komentirajte dobivene rezultate.
#import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Učitavanje podataka
# Zamijenite ovaj dio s vašim stvarnim podacima
# Pretpostavimo da su vaši podaci već učitani u numpy polje 'data'
data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
X = data[:, :-1]  # Ulazni podaci
y = data[:, -1]   # Izlazni podaci

# Podjela podataka na skup za učenje i skup za testiranje (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# a) Izgradnja modela logisticke regresije
model = LogisticRegression()
model.fit(X_train, y_train)

# b) Klasifikacija skupa podataka za testiranje
y_pred = model.predict(X_test)

# c) Izračun i prikaz matrice zabune na testnim podacima
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(conf_matrix)

# d) Izračun točnosti, preciznosti i odziva na skupu podataka za testiranje
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\nMetrike:")
print(f"Točnost: {accuracy}")
print(f"Preciznost: {precision}")
print(f"Odziv: {recall}")
