from flask import Flask, jsonify, request
from modules.appleId_check_db import ProfileExistence
from raven.contrib.flask import Sentry

app = Flask(__name__)
sentry = Sentry(app)


@app.route('/api/v1/search/id')
def appleId():

    query = request.args.get('q')
    obj = ProfileExistence()
    data = obj.db_check(query)
    return jsonify({'data':
                    {'availability': data['profileExists']}
                    }
                  )


if __name__ == '__main__':
    app.run(port=5009)
