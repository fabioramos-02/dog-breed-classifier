# Flask app para upload e classificação de imagem de cachorro
from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import os
from predict import predict_breed

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
	os.makedirs(app.config['UPLOAD_FOLDER'])

HTML_FORM = '''
<!doctype html>
<title>Classificador de Raça de Cachorro</title>
<h1>Envie a imagem de um cachorro</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Classificar>
</form>
{% if prediction %}
<h2>Raça prevista: {{ prediction }}</h2>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	prediction = None
	if request.method == 'POST':
		if 'file' not in request.files:
			return render_template_string(HTML_FORM, prediction=None)
		file = request.files['file']
		if file.filename == '':
			return render_template_string(HTML_FORM, prediction=None)
		if file:
			filename = secure_filename(file.filename)
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(filepath)
			prediction = predict_breed(filepath)
			os.remove(filepath)
	return render_template_string(HTML_FORM, prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)
