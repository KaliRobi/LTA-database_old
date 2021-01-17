from flask import Flask, request, render_template


app = Flask(__name__, template_folder='../templates')


@app.route('/')
def home():
    return render_template("smal_scale.html")


record_input = {'volume': '', 'id': '', 'name_with_aliases': '', 'sex': '', 'height_cm': '', 'build': '', 'dentition': '', 'special_peculiarities': '', 'date_of_birth': '', 'place_of_birth': '', 'place_of_residence': '', 'residence': '', 'religion': '', 'childhood_status': '', 'marital_status': '', 'number_of_children': '',
                'occupation': '', 'occupation_2': '', 'occupation_3': '', 'military_service': '', 'literacy': '',  'education': '', 'criminal_history': '', 'crime': '', 'sentence_begins': '', 'sentence_expires': '', 'prison_term': '', 'ransome': '', 'associates': '', 'degree_crime': '', 'degree_punishment': '', 'notes': '', 'arrest_site': ''}


@app.route('/post_data', methods=['POST'])
def post_data():
    volume = request.form['volume']
    record_input.update({'volume': volume})

    name = request.form['name']
    record_input.update({'name': name})

    sex = request.form['sex']
    record_input.update({'sex': sex})

    height = request.form['height']
    record_input.update({'height': height})

    build = request.form['build']
    record_input.update({'build': build})

    dentition = request.form['dentition']
    record_input.update({'dentition': dentition})

    special_peculiarities = request.form['special_peculiarities']
    record_input.update({'special_peculiarities': special_peculiarities})

    date_of_birth = request.form['date_of_birth']
    record_input.update({'date_of_birth': date_of_birth})

    place_of_birth = request.form['place_of_birth']
    record_input.update({'place_of_birth': place_of_birth})

    place_of_residence = request.form['place_of_residence']
    record_input.update({"place_of_residence": place_of_residence})

    residence = request.form['residence']
    record_input.update({"residence": residence})

    religion = request.form['religion']
    record_input.update({'religion': religion})

    childhood_status = request.form['childhood_status']
    record_input.update({'childhood_status': childhood_status})

    marital_status = request.form['marital_status']
    record_input.update({'marital_status': marital_status})

    number_of_children = request.form['number_of_children']
    record_input.update({'number_of_children': number_of_children})

    occupation = request.form['occupation']
    record_input.update({'occupation': occupation})

    occupation_2 = request.form['occupation_2']
    record_input.update({'occupation_2': occupation_2})

    occupation_3 = request.form['occupation_3']
    record_input.update({'occupation_3': occupation_3})

    military_service = request.form['military_service']
    record_input.update({'military_service': military_service})

    literacy = request.form['literacy']
    record_input.update({'literacy': literacy})

    education = request.form['education']
    record_input.update({'education': education})

    criminal_history = request.form['criminal_history']
    record_input.update({'criminal_history': criminal_history})

    crime = request.form['crime']
    record_input.update({'crime': crime})

    sentence_begins = request.form['sentence_begins']
    record_input.update({'sentence_begins': sentence_begins})

    sentence_expires = request.form['sentence_expires']
    record_input.update({'sentence_expires': sentence_expires})

    prison_term = request.form['prison_term']
    record_input.update({'prison_term': prison_term})

    ransome = request.form['ransome']
    record_input.update({'ransome': ransome})

    associates = request.form['associates']
    record_input.update({'associates': associates})

    degree_crime = request.form['degree_crime']
    record_input.update({'degree_crime': degree_crime})

    degree_punishment = request.form['degree_punishment']
    record_input.update({'degree_punishment': degree_punishment})

    notes = request.form['notes']
    record_input.update({'notes': notes})

    arrest_site = request.form['arrest_site']
    record_input.update({'arrest_site': arrest_site})

    return record_input


app.run(debug=True, port=5502)
