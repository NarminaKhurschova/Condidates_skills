from flask import Flask
from utils import load_candidates_list
my_app = Flask(__name__)

@my_app.route("/")
def main_page():
    candidates_new = ''
    for candidate in load_candidates_list():
        candidates_new += (f" Имя кандидата - {candidate['name']} \n Позиция кандидата {candidate['position']} \n Навыки {candidate['skills']} \n\n")
    return '<pre>'+candidates_new+'</pre>'

@my_app.route("/candidates/<int:x>")
def candidates_page(x):
    candidate_new = ''
    for candidate in load_candidates_list():
        if x == candidate['id']:
            candidate_new += (f" Имя кандидата - {candidate['name']} \n Позиция кандидата {candidate['position']} \n Навыки {candidate['skills']} \n\n")
            return f'<pre>{candidate_new}<pre><img src="{candidate["picture"]}">'

@my_app.route("/skills/<skill>")
def candidates_skills(skill):
    candidates_skill = ''
    for candidate in load_candidates_list():
        skills_list = candidate['skills'].lower().replace(" ","").split(",")
        if skill.lower() in skills_list:
            candidates_skill += (f" Имя кандидата - {candidate['name']} \n Позиция кандидата {candidate['position']} \n Навыки {candidate['skills']} \n\n")
    return f'<pre>{candidates_skill}<pre>'

my_app.run()