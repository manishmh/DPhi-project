from flask import Flask, render_template, redirect, request
import os
import csv
 
# declare the Flask function in varibale app
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# use this code to route all other pages.
@app.route('</string:page_name>')
def html_page(page_name):
 	return render_template(page_name)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
