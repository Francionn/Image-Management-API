from app import app, repo
from flask import send_file,  abort, render_template, url_for, redirect, request
from datetime import datetime
from werkzeug.utils import secure_filename
import os


if not os.path.exists('uploads'):
    os.makedirs('uploads')


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.template_filter('datetime')
def datetime_filter(value, format='%Y-%m-%d %H:%M:%S'):
    if value is None:
        return ""
    
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    
    return value.strftime(format)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/gallery', methods=['GET'])
def gallery():
    
    data = repo.select()
    posts = [data_get.to_dict() for data_get in data]
    
    return render_template('gallery.html', posts = posts)

  
@app.route('/galeria/<int:id>', methods=['GET'])
def get_imagem(id):
    posts = repo.select()
    
    for post_get in posts:
        
        if post_get.id == id:
            post = post_get.to_dict()
            
            return render_template('image.html', post = post)
    
    return abort(404, description="Image not found")


@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    repo.delete(id)
    return redirect(url_for('gallery'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    if request.method == 'POST':
        new_description = request.form['descrip']
        repo.update(id, new_description)
        return redirect(url_for('gallery'))
    
    post = repo.select()
    for post_get in post:
        if post_get.id == id:
            post = post_get.to_dict()
            break
    else:
        return abort(404, description="Image not found")
    
    return render_template('update.html', post=post)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part", 400
        
        file = request.files['image']
        if file.filename == '':
            return "No selected file", 400
        
        if not allowed_file(file.filename):
            return "File type not allowed", 400
        
        description = request.form['descrip']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            file.save(filepath)
            repo.insert(filepath, description)
            return redirect(url_for('gallery'))
    
    return render_template('add.html')