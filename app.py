from flask import Flask, render_template, request
import diag as cdiag


app = Flask(__name__)
resource_dir = 'static/resource'
print('Hello')


@app.route('/')
def top():
    return render_template('index.html')
    # return render_template('index.html', host_list=host_list)


@app.route('/diag')
def diag():
    return render_template('diag.html')


@app.route('/get_diag')
def get_diag():
    try:
        if request.method == 'GET':
            target = request.args.get('target', '')
            print(f'selected: {target}')
    except Exception as e:
        return str(e)

    cdiag.target_list(target)
    neighbor_list = cdiag.target_list(target)
    # diag_list = cdiag.create_cli_diag(neighbor_list)
    # cdiag.show_cli_diag(diag_list)

    return render_template('diag.html', neighbor_list=neighbor_list)


# @app.route('/call_cli')
# def call_cli():
#     try:
#         if request.method == 'GET':
#             host = request.args.get('host', '')
#             print(f'clicall: {host}')
#     except Exception as e:
#         return str(e)

#     ping_result = ping.ping_cmd_args(host)
#     print('\n--- ping_result ---')
#     pprint.pprint(ping_result)

#     return render_template('index.html', host=host, ping_result=ping_result)


# @app.errorhandler(404)
# def redirect_main_page(error):
#    return render_template(url_for('top'))


if __name__ == '__main__':
    print('World')
    app.run(debug=True)
    # app.run(host='0.0.0.0')
