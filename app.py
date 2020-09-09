from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

import os
from configparser import ConfigParser

locations = []
descriptions=[]
headers=[]
for root, dirs, files in os.walk(os.curdir):
    for file in files:
        if file.endswith("index.html") & (root != os.curdir):
            locations.append(os.path.join(os.path.abspath(root),file))
            if os.path.isfile(os.path.join(root,'Description.ini')):                
                config = ConfigParser()
                config.read(os.path.join(root,'Description.ini'))
                descriptions.append(config.get('DOCUMENTATION', 'description'))
                headers.append(config.get('DOCUMENTATION', 'header'))
                
            else:
                descriptions.append('')
                headers.append(root)

@app.route("/")
def template_test():
    return render_template('template.html', locations=locations, descriptions=descriptions, headers=headers)


if __name__ == '__main__':
    app.run(debug=True, port=8089)