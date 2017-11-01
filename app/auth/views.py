from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    referer = request.args.get('referer', None)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            if referer is not None:
                referer = referer.strip() + "?ticket=" + _makeTicket()
            else:
                referer = url_for('main.index')
            return redirect(referer)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form, **dict(referer=referer))


def _makeTicket():
    return current_user.name


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data,
                    password=form.password.data,
                    stu_id=form.stu_id.data
                    )
        db.session.add(user)
        db.session.commit()
        flash('Register Success.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
