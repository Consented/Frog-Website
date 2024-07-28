from flask import Flask, render_template, url_for
from random import randint
app = Flask(__name__)


@app.route("/")
def hello():
    abs_img = url_for('static', filename='images/abstract_preview.png')
    d3_img = url_for('static', filename='images/3d_preview.png')
    part_img = url_for('static', filename='images/particle_preview.png')
    return render_template('home.html', random=randint(0,6), title="Home", abs_img=abs_img, d3_img=d3_img, part_img=part_img)

@app.route("/about")
def about():
    nav_img = url_for('static', filename='images/orangefrog.png')
    return render_template('about.html', title="About", nav_img = nav_img)

@app.route("/projects") 
def projects():
    nav_img = url_for('static', filename='images/greyfrog.png')
    return render_template('projects.html', title="Projects", nav_img = nav_img)
@app.route("/abstract_path")
def abstract_path():

    return render_template('abstract_path.html', title="Abstract Path")




# if __name__ == '__main__': Allows flask to be run when poorgram is run
#     app.run()
