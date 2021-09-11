from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '''
        <h1>Zitti e Buoni!</h1>
        <p>Parla, la gente purtroppo parla
        <p>Non sa di che cosa parla</p>
        <p>Tu portami dove sto a galla</p>
        <p>Che qui mi manca l'aria</p>
        <br>
        <br>
        <p>Остерегайтесь печенек.<p>
        '''
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            res = 'http://myvm.localhost/\n'
            for key in data:
                params = json.loads(key)
                for i in range(params['count']):
                    res += f'{params["animal"]} says {params["sound"]}\n'
                res += 'Made with ❤️ by Evgeny Frolov\n'
                return res
        except:
            return 'Incorrect data'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {} 😎!</h1>\nДальше вы не пройдете, пока не получите бумаги.'.format(name.capitalize())


if __name__ == '__main__':
    app.run(port=80)  # debug=True
