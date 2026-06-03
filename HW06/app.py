import flask

import os
import utils

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/posters')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def starter_page():

    ganres_list = utils.load_file('ganres_list.json')
    if flask.request.method == 'POST':

        ganre_name = flask.request.form['ganre_name']
        ganres_list.append(ganre_name)
        utils.save_file('ganres_list.json', ganres_list)
        utils.save_file(f'{ganre_name}.json', [])

    return flask.render_template('index.html', ganres_list=ganres_list)


@app.route('/genres/<ganre_name>', methods=['GET', 'POST'])
def show_film_list(ganre_name):

    film_list = utils.load_file(f'{ganre_name}.json')
    if flask.request.method == 'POST':

        film_list.append(utils.make_dict())
        utils.save_file(f'{ganre_name}.json', film_list)

    return flask.render_template('film_list.html', gnr_name=ganre_name, flm_lst=film_list)


@app.route('/genres/<ganre_name>/<film_id>', methods=['GET', 'PUT'])
def show_film_details(ganre_name, film_id):

    films = utils.load_file(f'{ganre_name}.json')

    if flask.request.method == 'PUT':
        updated_film = flask.request.get_json()
        film = films[int(film_id) - 1]
        for key, value in updated_film.items():
            film[key] = value
        utils.save_file(f'{ganre_name}.json', films)
    film = films[int(film_id) - 1]
    return flask.render_template('film.html', film=film, film_id=int(film_id), ganre_name=ganre_name)


@app.route('/about')
def about():
    return flask.render_template('about.html')


app.run(debug=True)
