from flask import Flask,render_template,request
import pandas as pd
import pickle

app = Flask(__name__, template_folder="template")
model = pickle.load(open("./lgbm.pkl", "rb"))
print("Model Loaded")

@app.route("/")
def home():
	return render_template("predictor.html")

@app.route("/predict",methods=['POST'])
def predict():
	if request.method == "POST":
		# DATE
		Date = request.form['date']

		Month = int(pd.to_datetime(Date).month)
		

		Season=[]
		if (Month == 12 or Month == 1 or Month == 2):
			Season.append(1)  	#Summer
		elif (Month == 3 or Month == 4 or Month == 5):
			Season.append(2)	 #Autumn

		elif (Month == 6 or Month == 7 or Month == 8):
			Season.append(3)	#Winter
		else:
			Season.append(4)	# Spring

		# MinTemp
		MinTemp = float(request.form['mintemp'])

		# # MaxTemp
		MaxTemp = float(request.form['maxtemp'])

		# # Evaporation
		Evaporation = float(request.form['evaporation'])

		# # Sunshine
		Sunshine = float(request.form['sunshine'])

		# # Wind Gust Speed
		WindGustSpeed = float(request.form['windgustspeed'])

		# # Wind Speed 9am
		WindSpeed9am = float(request.form['windspeed9am'])

		# # Wind Speed 3pm
		WindSpeed3pm = float(request.form['windspeed3pm'])

		# # Humidity 9am
		Humidity9am = float(request.form['humidity9am'])

		# # Humidity 3pm
		Humidity3pm = float(request.form['humidity3pm'])

		# # Pressure 9am
		Pressure9am = float(request.form['pressure9am'])

		# # Cloud 9am
		Cloud9am = float(request.form['cloud9am'])

		# # Cloud 3pm
		Cloud3pm = float(request.form['cloud3pm'])

		# # Location
		Location = float(request.form['location'])

		# # Wind Dir 9am
		WindDir9am = float(request.form['winddir9am'])

		# # Wind Dir 3pm
		WindDir3pm = float(request.form['winddir3pm'])

		# # Wind Gust Dir
		WindGustDir = float(request.form['windgustdir'])

		# # Rain Today
		RainToday = float(request.form['raintoday'])



		data={'Location':Location,'MinTemp':MinTemp,'MaxTemp':MaxTemp,'Evaporation':Evaporation,'Sunshine':Sunshine,
				'WindGustDir':WindGustDir,'WindGustSpeed':WindGustSpeed,'WindDir9am':WindDir9am,'WindDir3pm':WindDir3pm,
			  'WindSpeed9am':WindSpeed9am,'WindSpeed3pm':WindSpeed3pm,'Humidity9am':Humidity9am,'Humidity3pm':Humidity3pm,
			  'Pressure9am':Pressure9am,'Cloud9am':Cloud9am,'Cloud3pm':Cloud3pm,'RainToday':RainToday,
			'Month':Month,'Season':Season}


		df=pd.DataFrame(data)
		pred = model.predict(df)

		print(pred[0])
		if pred[0] == 0:
			return render_template("after_sunny.html")
		else:
			return render_template("after_rainy.html")


	return render_template("predictor.html")

if __name__=='__main__':
	app.run(debug=True)