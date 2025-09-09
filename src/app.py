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
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Classificador de Raça de Cachorro</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container py-5">
	<div class="row justify-content-center">
		<div class="col-md-6">
			<div class="card shadow">
				<div class="card-body">
					<h2 class="card-title mb-4 text-center">Classificador de Raça de Cachorro</h2>
					<form method="post" enctype="multipart/form-data">
						<div class="mb-3">
							<input class="form-control" type="file" name="file" required>
						</div>
						<div class="d-grid">
							<button class="btn btn-primary" type="submit">Classificar</button>
						</div>
					</form>
					{% if prediction %}
						<div class="alert alert-success mt-4 text-center">
							<strong>Raça prevista:</strong> {{ prediction }}
						</div>
					{% endif %}
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>
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
