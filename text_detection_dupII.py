import os

from util.func import *
from pathlib import Path
from db.PsyDb import Database
from selenium import webdriver
from util.func import allowed_file
from werkzeug.utils import secure_filename
from util.PyConstant import name, cp, dust
from flask import Flask, render_template, request, flash, redirect, url_for


UPLOAD_FOLDER = '/home/hdc/Downloads/project/py3cv4/png'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '123456'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/for')
def hello_for():
    check_list = request.form.getlist('hello')
    print(check_list)
    return render_template('for.html', items=['ron', 'wu'], check=check_list)


@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if os.path.isdir(app.config['UPLOAD_FOLDER']):
                if not os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                os.makedirs(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))
    return render_template('up.html')


if __name__ == '__main__':
    os.environ[GOOGLE_APPLICATION_CREDENTIALS] = key_path
    my_db = Database(database, user, password, host)
    my_db.execute("select file_name from files;")
    exist_files = [x[0] for x in my_db.fetchall()]
    for i in walk_folder(root_folder):
        if len(i) > 0:
            if walk_folder(root_folder).index(i) == 0:
                for file1 in i:
                    if file1[-12:] not in exist_files:
                        read_detection(db=my_db, input_file=file1, box=fix_box2, cp_len=2,
                                       debug=false_flag, ocr_cfg1=psm7_oem1_number,
                                       ocr_cfg2=psm7_oem1_config_words, file_name=file1[-12:])
            elif walk_folder(root_folder).index(i) == 1:
                for file2 in i:
                    if file2[-12:] not in exist_files:
                        read_detection(db=my_db, input_file=file2, box=fix_box3, cp_len=3,
                                       debug=false_flag, ocr_cfg1=psm7_oem1_number,
                                       ocr_cfg2=psm7_oem1_config_words, file_name=file2[-12:])
            elif walk_folder(root_folder).index(i) == 2:
                for file3 in i:
                    if file3[-12:] not in exist_files:
                        read_detection(db=my_db, input_file=file3, box=fix_box4, cp_len=4,
                                       debug=false_flag, ocr_cfg1=psm7_oem1_number,
                                       ocr_cfg2=psm7_oem1_config_words, file_name=file3[-12:])

    for x, y, _ in os.walk(root_folder):
        for i in y:
            clean_up(os.path.join(x, i))

    driver = webdriver.Firefox(executable_path='/home/hdc/Downloads/project/py3cv4/geckodriver/geckodriver')
    driver.maximize_window()
    driver.get("https://pokeassistant.com/main/ivcalculator")
    cook_accept(driver)
    my_db.execute(select_bugs)
    for i in my_db.fetchall():
        # print(i)
        if false_flag:
            print(i)
            print(type(i[1]))
        if i[0] == name and int(i[1]) <= cp and int(i[2]) >= dust:
            my_db.execute(update_useless_bug, ("true", i[5]))
            my_db.commit()
        elif i[0] == name and int(i[1]) <= cp and int(i[2]) <= dust:
            if do_calculation(driver, name_changed=False, name=i[0],
                              cp=str(i[1]), hp=str(i[2]), dust=str(i[3]), debug=false_flag):
                bug_result = check_results(driver)
                if false_flag:
                    print(bug_result)
                if len(bug_result) == 3:
                    my_db.execute(insert_into_results, (i[0], int(i[1]), int(i[3]), float(bug_result[0]),
                                                        float(bug_result[1]), float(bug_result[2]), i[5]))
                    my_db.execute(update_checked_bug, ("true", i[5]))
                    my_db.commit()
            else:
                print("check {} failed!".format(i[5]))
        elif i[0] != name:
            if do_calculation(driver, name_changed=True, name=i[0],
                              cp=str(i[1]), hp=str(i[2]), dust=str(i[3]), debug=false_flag):
                bug_result = check_results(driver)
                if false_flag:
                    print(bug_result)
                if len(bug_result) == 3:
                    my_db.execute(insert_into_results, (i[0], int(i[1]), int(i[3]), float(bug_result[0]),
                                                        float(bug_result[1]), float(bug_result[2]), i[5]))
                    my_db.execute(update_checked_bug, ("true", i[5]))
                    my_db.commit()
            else:
                print("check {} failed!".format(i[5]))
        name, cp, dust = i[0], int(i[1]), int(i[3])
    driver.quit()
    my_db.exit()
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0')

