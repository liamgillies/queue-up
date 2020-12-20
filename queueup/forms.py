from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from queueup.models import User


LOL_RANKS = [
    {'name': 'Challenger', 'rank': 26},
    {'name': 'Grandmaster', 'rank': 25},
    {'name': 'Master', 'rank': 24},
    {'name': 'Diamond I', 'rank': 23},
    {'name': 'Diamond II', 'rank': 22},
    {'name': 'Diamond III', 'rank': 21},
    {'name': 'Diamond IV', 'rank': 20},
    {'name': 'Platinum I', 'rank': 19},
    {'name': 'Platinum II', 'rank': 18},
    {'name': 'Platinum III', 'rank': 17},
    {'name': 'Platinum IV', 'rank': 16},
    {'name': 'Gold I', 'rank': 15},
    {'name': 'Gold II', 'rank': 14},
    {'name': 'Gold III', 'rank': 13},
    {'name': 'Gold IV', 'rank': 12},
    {'name': 'Silver I', 'rank': 11},
    {'name': 'Silver II', 'rank': 10},
    {'name': 'Silver III', 'rank': 9},
    {'name': 'Silver IV', 'rank': 8},
    {'name': 'Bronze I', 'rank': 7},
    {'name': 'Bronze II', 'rank': 6},
    {'name': 'Bronze III', 'rank': 5},
    {'name': 'Bronze IV', 'rank': 4},
    {'name': 'Iron I', 'rank': 3},
    {'name': 'Iron II', 'rank': 2},
    {'name': 'Iron III', 'rank': 1},
    {'name': 'Iron IV', 'rank': 0}]

LOL_ROLES = ['top', 'jungle', 'middle', 'bottom', 'support']



class ProfileForm(FlaskForm):
    ign = StringField('in game name', validators=[DataRequired()])
    rank = SelectField('select your rank', choices=[a['name'] for a in LOL_RANKS], validators=[DataRequired()]);
    roles = SelectMultipleField('select your role(s)', choices=LOL_ROLES, validators=[DataRequired()]);
    opgg = StringField('enter op.gg link', validators=[DataRequired()])
    description = TextAreaField('describe yourself', validators=[DataRequired()])
    # picture = FileField('upload pfp', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    rolesLF = SelectMultipleField('select your role(s)', choices=LOL_ROLES);
    lowRankLF = SelectField('select low rank', choices=[a['name'] for a in LOL_RANKS], validators=[DataRequired()]);
    highRankLF = SelectField('select high rank', choices=[a['name'] for a in LOL_RANKS], validators=[DataRequired()]);

    submit = SubmitField('save')