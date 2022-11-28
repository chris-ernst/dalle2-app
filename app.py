from flask import Flask, render_template, request, url_for, flash, redirect
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '723a5f52d35b009faa65c12defc57f4363a1b6f80978aac4'


# with open('data.json') as json_file:
#     data_json = json.load(json_file)
 
#     # Print the type of data variable
#     print("Type:", type(data_json))
 
#     # Print the data of dictionary
#     print("\ncards:", data_json['cards'])


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/work')
def work():
    with open('data.json') as json_file:
        data_json = json.load(json_file)
    return render_template('work.html', cards=data_json["cards"])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/36b96148e9a4', methods=('GET', 'POST'))
def admin():

    with open('data.json') as json_file:
        data_json = json.load(json_file)

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
            data_json['cards'].append({'image': image, 'title': title, 'material': material, 'description': description})
            
            with open("data.json", "w") as outfile:
                json.dump(data_json, outfile)

            print("\ncards:", data_json['cards'])
            return redirect(url_for('work'))


    return render_template('admin.html')