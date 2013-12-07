@app.route('/upload', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename: 
			filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)
    return render_template('index.html')
 
@app.route('/uploads/')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)
