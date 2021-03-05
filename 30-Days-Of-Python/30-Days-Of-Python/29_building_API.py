from flask import Flask, Response
import json
import os

app = Flask(__name__)


@app.route('/api/v1.0/users', methods=['GET'])
def users():
    user_list = [
        {
            'name': 'Zhang San',
            'country': 'China',
            'city': 'Hangzhou',
            'skills': ['Java', '.NET', 'Python']
        },
        {
            'name': 'Li Si',
            'country': 'China',
            'city': 'Shanghai',
            'skills': ['JavaScript', 'Vue', 'React']
        },
        {
            'name': 'Jack',
            'country': 'American',
            'city': 'Washington',
            'skills': ['Java', 'JavaScript', 'Python']
        }
    ]
    return Response(json.dumps(user_list), mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host = '0.0.0.0', port=port)
