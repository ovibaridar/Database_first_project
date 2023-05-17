from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_wtf import FlaskForm, RecaptchaField
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Ledn0kjAAAAALaHKtFr6RbJvxxDrjJRzoT2W3su'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Ledn0kjAAAAAPbBy527aHtDIW2kIky7z0MtxS1t'
app.config['TESTING'] = True
app.config['UPLOAD_FOLDER '] = "static/img"


class reg(FlaskForm):
    recaptcha = RecaptchaField()


main = None


@app.route('/')
def home():
    form = reg()
    return render_template('reg.html', form=form)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbms_project"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        batch = request.form['batch']
        semester = request.form['semester']
        gender = request.form['g']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        address = request.form['address']
        photo = request.files['photo']


        if photo == '' or name == '' or id == '' or batch == '' or batch == 'Batch' or semester == '' or gender == '' or email == '' or password == '' or c_password == '' or address == '':
            error = "Your data is empty somewhere"
            form = reg()
            return render_template('reg.html', form=form, error=error ,name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)
        if len(id)!=11:
            idlenerror = "Your id length is less or more than  11"
            form = reg()
            return render_template('reg.html', form=form, idlenerror=idlenerror, name=name, address=address, batch=batch,
                                   id=id, email=email, gender=gender, semester=semester, password=password,
                                   c_password=c_password)

        if len(password) < 8:
            passlen = "Password is less than 8 characters"
            form = reg()
            return render_template('reg.html', form=form, passlen=passlen ,name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)
        if password != c_password:
            passerr = "Passwords do NOT match"
            form = reg()
            return render_template('reg.html', form=form, passerr=passerr ,name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)
        if photo.filename == '':
            err = "Import Your Image"
            form = reg()
            return render_template('reg.html', form=form, err=err ,name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)
        if len(photo.filename) > 99:
            long = "File name is too long"
            form = reg()
            return render_template('reg.html', form=form, long=long , name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)

        mycursor.execute("select * from registration where student_id = '" + id + "' ")
        id_data = mycursor.fetchall()
        if len(id_data) != 0:
            iderr = "This id is already add"
            form = reg()
            return render_template('reg.html', form=form, iderr=iderr , name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)

        else:
            photoname = photo.filename
            size = len(photoname) - 3
            p = len(photoname) - (size + 1)
            n = len(photoname) - (size + 2)
            g = len(photoname) - (size + 3)
            filetype = photoname[size] + photoname[size + 1] + photoname[size + 2]
            jpg = "jpg"
            png = "png"
            if filetype == jpg or filetype == "JPG" or filetype == png or filetype == "png":
                filep = os.path.join(app.config['UPLOAD_FOLDER '], id + photo.filename)
                photo.save(filep)
                photoname = id + photo.filename
                mycursor.execute(
                    "insert into registration (Name,Batch,student_id,semister,gender,email,password,address,photo)value(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (name, batch, id, semester, gender, email, password, address, photoname))
                mydb.commit()
                mycursor.close()
                return redirect('/dashboard')
            else:
                typeprb = "Only jpg and png file are supported "
                form = reg()
                return render_template('reg.html', form=form, typeprb=typeprb, name=name, address=address, batch=batch,
                                       id=id, email=email, gender=gender, semester=semester, password=password,
                                       c_password=c_password)


@app.route('/dashboard')
def dash():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbms_project"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from registration")
    student_all_data = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    return render_template('data-table.html', datas=student_all_data)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbms_project"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        id = request.form['ID']
        mycursor.execute("delete from  registration where student_id = '" + id + "'")
        mydb.commit()
        mycursor.close()
        return redirect('/dashboard')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbms_project"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        batch = request.form['batch']
        semester = request.form['semester']
        gender = request.form['gender']
        oldpass = request.form['oldpass']
        newpass = request.form['newpass']
        cnewpass = request.form['cnewpass']
        photo = request.files['photo']
        address = request.form['address']


        mycursor.execute("select * from  registration where student_id ='" + id + "'")
        id_data = mycursor.fetchone()

        if id_data == 0:

            idnotmatch = "Your id is not match try  again "
            mycursor.execute("select * from registration")
            student_all_data = mycursor.fetchall()
            mydb.commit()
            mycursor.close()
            return render_template('data-table.html', datas=student_all_data, idnotmatch=idnotmatch)

        else:

            mycursor.execute("select  *  from registration where student_id ='" + id + "'")
            dataPass = mycursor.fetchone()
            Pass = dataPass[6]
            if Pass != oldpass:
                idnotmatch = "Your Old password is not match try  again "
                mycursor.execute("select * from registration")
                student_all_data = mycursor.fetchall()
                mydb.commit()
                mycursor.close()
                return render_template('data-table.html', datas=student_all_data, idnotmatch=idnotmatch)

            else:

                if newpass != cnewpass:
                    idnotmatch = "Your password is not match try  again "
                    mycursor.execute("select * from registration")
                    student_all_data = mycursor.fetchall()
                    mydb.commit()
                    mycursor.close()
                    return render_template('data-table.html', datas=student_all_data, idnotmatch=idnotmatch)

                else:

                    if photo.filename == '':
                        if newpass != '' or cnewpass != '':
                          mycursor.execute(
                             "update registration set Name ='" + name + "',Batch='" + batch + "',semister='" + semester + "',gender='" + gender + "',email='" + email + "',password='" + newpass + "',address='" + address + "' where student_id = '" + id + "' ")
                          mydb.commit()
                          mycursor.close()
                          return redirect('/dashboard')
                        else:
                            mycursor.execute(
                                "update registration set Name ='" + name + "',Batch='" + batch + "',semister='" + semester + "',gender='" + gender + "',email='" + email + "',address='" + address + "' where student_id = '" + id + "' ")
                            mydb.commit()
                            mycursor.close()
                            return redirect('/dashboard')


                    else:
                        photoname = photo.filename
                        size = len(photoname) - 3
                        p = len(photoname) - (size + 1)
                        n = len(photoname) - (size + 2)
                        g = len(photoname) - (size + 3)
                        filetype = photoname[size] + photoname[size + 1] + photoname[size + 2]
                        jpg = "jpg"
                        png = "png"
                        if filetype == jpg or filetype == "JPG" or filetype == png or filetype == "png":
                            if newpass=='' or cnewpass=='':
                                filep = os.path.join(app.config['UPLOAD_FOLDER '], id + photo.filename)
                                photo.save(filep)
                                photoname = id + photo.filename
                                mycursor.execute(
                                    "update registration set Name ='" + name + "',Batch='" + batch + "',semister='" + semester + "',gender='" + gender + "',email='" + email + "',address='" + address + "',photo='" + photoname + "' where student_id = '" + id + "' ")
                                mydb.commit()
                                mycursor.close()
                                return redirect('/dashboard')
                            else:
                                filep = os.path.join(app.config['UPLOAD_FOLDER '], id + photo.filename)
                                photo.save(filep)
                                photoname = id + photo.filename
                                mycursor.execute(
                                    "update registration set Name ='" + name + "',Batch='" + batch + "',semister='" + semester + "',gender='" + gender + "',email='" + email + "',password='" + newpass + "',address='" + address + "',photo='" + photoname + "' where student_id = '" + id + "' ")
                                mydb.commit()
                                mycursor.close()
                                return redirect('/dashboard')

                        else:
                            idnotmatch = "Only  JPG and PNG file  supported"
                            mycursor.execute("select * from registration")
                            student_all_data = mycursor.fetchall()
                            mydb.commit()
                            mycursor.close()
                            return render_template('data-table.html', datas=student_all_data, idnotmatch=idnotmatch)





app.debug = True
app.run(host='0.0.0.0', port=8111)
