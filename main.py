from flask import Flask, render_template, request, flash, redirect
from forms import FormLogin, FormCriarConta
app = Flask(__name__)
app.config['SECRET_KEY'] = 'afdsjifdsajkfdsjakfdsafdaads'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/?')
def contato():

    return render_template('result.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect('/')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect('/')

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)



@app.route('/assinatura')
def assinatura():

    return render_template('assinatura.html')


if __name__ == '__main__':
    app.run(debug=True)
