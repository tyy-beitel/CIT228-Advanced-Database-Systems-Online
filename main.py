from flask import Flask, render_template, request, session
import random

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
      user_choice = request.form['choice']
      if user_choice not in['rock', 'paper', 'scissors']:
        return render_template('index.html', message = 'Not a valid choice, try again')
      session['user_choice'] = user_choice
      ai_choice = random.choice(['rock', 'paper', 'scissors'])
      session['ai_choice'] = ai_choice
      results = game_win(user_choice, ai_choice)
      session['results'] = results
      return render_template('base.html', user_choice=user_choice.capitalize(), ai_choice=ai_choice.capitalize(), results=results)
    return render_template('index.html')

def game_win(user_choice, ai_choice):
  if user_choice == ai_choice:
    return 'It was a tie'
  elif user_choice == 'rock':
    if ai_choice == 'paper':
      return 'AI wins!'
    else:
      return 'You win!'
  elif user_choice == 'paper':
    if ai_choice == 'scissors':
      return 'AI wins!'
    else:
      return 'You win!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
