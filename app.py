from flask import Flask, render_template, request, url_for, flash, redirect, abort
import json, sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '723a5f52d35b009faa65c12defc57f4363a1b6f80978aac4'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/work')
def work():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('work.html', posts=posts)

@app.route('/work_grid')
def work_grid():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('work_grid.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/36b96148e9a4')
def admin():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('admin.html', posts=posts)


@app.route('/36b96148e9a4/add_new', methods=('GET', 'POST'))
def add_new():
    if request.method == 'POST':
        image = request.form['my_file_input']
        title = request.form['title']
        material = request.form['material']
        description = request.form['description']
        #category = request.form['category']

        if not image:
            flash('Image is required!')
        elif not title:
            flash('Title is required!')
        elif not material:
            flash('Matrial is required!')
        elif not description:
            flash('Description is required!')
        else:

            conn = get_db_connection()
            conn.execute('INSERT INTO posts (image, title, material, description) VALUES (?, ?, ?, ?)',
                            (image, title, material, description))
            conn.commit()
            conn.close()
            return redirect(url_for('admin'))
    return render_template('add_new.html')



@app.route('/36b96148e9a4/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        image = request.form['my_file_input']
        title = request.form['title']
        material = request.form['material']
        description = request.form['description']

        if not image:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET  title = ?, material = ?, description = ?'
                         ' WHERE id = ?',
                         (title, material, description, id))
            conn.commit()
            conn.close()
            return redirect(url_for('admin'))
            
        elif not title:
            flash('Title is required!')
        elif not material:
            flash('Matrial is required!')
        elif not description:
            flash('Description is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET image = ?, title = ?, material = ?, description = ?'
                         ' WHERE id = ?',
                         (image, title, material, description, id))
            conn.commit()
            conn.close()
            return redirect(url_for('admin'))

    return render_template('edit.html', post=post)


@app.route('/36b96148e9a4/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('admin'))