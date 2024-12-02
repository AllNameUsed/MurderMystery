from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

# Dictionary to map access codes to mp3 files
access_code_to_file = {
    "12345": "lady.mp3",
    "54321": "butler.mp3",
    "42354": "daughter.mp3",
    "02211": "doctor.mp3",
    "49877": "groundskeeper.mp3",
    "31107": "historian.mp3",
    "82427": "jouranlist.mp3",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        access_code = request.form.get('access_code')
        if access_code in access_code_to_file:
            # If code is correct, play corresponding file
            audio_file = access_code_to_file[access_code]
            return render_template('index.html', audio_file=audio_file)
        else:
            # If code is incorrect, flash a toast notification
            flash("Incorrect access code. Please try again.")
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
