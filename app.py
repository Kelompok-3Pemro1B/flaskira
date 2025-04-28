'''
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penulis = db.Column(db.String(100), nullable=False)
    judul_buku = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Penulis': self.penulis,
            'Judul Buku': self.judul_buku,
            'Harga': self.harga
        }

# Membuat database pertama kali
with app.app_context():
    db.create_all()
    print("Database berhasil dibuat atau sudah ada.")
    

# CRUD API

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    new_book = Book(
        penulis=new_data['Penulis'],
        judul_buku=new_data['Judul Buku'],
        harga=new_data['Harga']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        if 'Penulis' in updated_data:
            book.penulis = updated_data['Penulis']
        if 'Judul Buku' in updated_data:
            book.judul_buku = updated_data['Judul Buku']
        if 'Harga' in updated_data:
            book.harga = updated_data['Harga']
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi untuk MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/nama_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Setup MySQL
mysql = MySQL(app)

# Model database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penulis = db.Column(db.String(100), nullable=False)
    judul_buku = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Penulis': self.penulis,
            'Judul Buku': self.judul_buku,
            'Harga': self.harga
        }

# Membuat database pertama kali
with app.app_context():
    db.create_all()
    print("Database berhasil dibuat atau sudah ada.")

# CRUD API

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    new_book = Book(
        penulis=new_data['Penulis'],
        judul_buku=new_data['Judul Buku'],
        harga=new_data['Harga']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        if 'Penulis' in updated_data:
            book.penulis = updated_data['Penulis']
        if 'Judul Buku' in updated_data:
            book.judul_buku = updated_data['Judul Buku']
        if 'Harga' in updated_data:
            book.harga = updated_data['Harga']
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

# Halaman Home (untuk GUI)
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Menambahkan buku melalui form HTML
@app.route('/add_book', methods=['POST'])
def add_book_from_form():
    penulis = request.form['penulis']
    judul_buku = request.form['judul_buku']
    harga = request.form['harga']
    
    new_book = Book(penulis=penulis, judul_buku=judul_buku, harga=harga)
    db.session.add(new_book)
    db.session.commit()

    return render_template('index.html', books=Book.query.all())

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi untuk MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/booksmy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Model database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penulis = db.Column(db.String(100), nullable=False)
    judul_buku = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Penulis': self.penulis,
            'Judul Buku': self.judul_buku,
            'Harga': self.harga
        }

# Membuat database pertama kali
with app.app_context():
    db.create_all()
    print("Database berhasil dibuat atau sudah ada.")

# CRUD API

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    new_book = Book(
        penulis=new_data['Penulis'],
        judul_buku=new_data['Judul Buku'],
        harga=new_data['Harga']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        if 'Penulis' in updated_data:
            book.penulis = updated_data['Penulis']
        if 'Judul Buku' in updated_data:
            book.judul_buku = updated_data['Judul Buku']
        if 'Harga' in updated_data:
            book.harga = updated_data['Harga']
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

# Halaman Home (untuk GUI)
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Menambahkan buku melalui form HTML
@app.route('/add_book', methods=['POST'])
def add_book_from_form():
    penulis = request.form['penulis']
    judul_buku = request.form['judul_buku']
    harga = request.form['harga']
    
    new_book = Book(penulis=penulis, judul_buku=judul_buku, harga=harga)
    db.session.add(new_book)
    db.session.commit()

    return render_template('index.html', books=Book.query.all())

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # untuk flash message

# Konfigurasi untuk MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/booksmy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Model database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penulis = db.Column(db.String(100), nullable=False)
    judul_buku = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Penulis': self.penulis,
            'Judul Buku': self.judul_buku,
            'Harga': self.harga
        }

# Membuat database pertama kali
with app.app_context():
    db.create_all()
    print("Database berhasil dibuat atau sudah ada.")

# CRUD API (untuk Postman / API)
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    new_book = Book(
        penulis=new_data['Penulis'],
        judul_buku=new_data['Judul Buku'],
        harga=new_data['Harga']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        if 'Penulis' in updated_data:
            book.penulis = updated_data['Penulis']
        if 'Judul Buku' in updated_data:
            book.judul_buku = updated_data['Judul Buku']
        if 'Harga' in updated_data:
            book.harga = updated_data['Harga']
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

# --- GUI ROUTES ---

# Halaman Home
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Tambah Buku lewat Form HTML
@app.route('/add_book', methods=['POST'])
def add_book_from_form():
    penulis = request.form['penulis']
    judul_buku = request.form['judul_buku']
    harga = request.form['harga']
    
    new_book = Book(penulis=penulis, judul_buku=judul_buku, harga=harga)
    db.session.add(new_book)
    db.session.commit()

    flash('Buku berhasil ditambahkan!', 'success')
    return redirect(url_for('home'))

# Cari Buku berdasarkan ID lewat Form HTML
@app.route('/get_book', methods=['GET'])
def get_book_by_id_form():
    book_id = request.args.get('id')
    if not book_id:
        flash('ID buku harus diisi.', 'danger')
        return redirect(url_for('home'))
    
    book = Book.query.get(book_id)
    if not book:
        flash(f'Buku dengan ID {book_id} tidak ditemukan.', 'danger')
        return redirect(url_for('home'))

    return render_template('book_detail.html', book=book)

# Update Buku lewat Form HTML
@app.route('/update_book', methods=['POST'])
def update_book_from_form():
    book_id = request.form.get('id')
    book = Book.query.get(book_id)

    if not book:
        flash(f'Buku dengan ID {book_id} tidak ditemukan.', 'danger')
        return redirect(url_for('home'))

    book.penulis = request.form['penulis']
    book.judul_buku = request.form['judul_buku']
    book.harga = request.form['harga']

    db.session.commit()
    flash(f'Buku ID {book_id} berhasil diperbarui!', 'success')
    return redirect(url_for('home'))

# Hapus Buku lewat Form HTML
@app.route('/delete_book', methods=['POST'])
def delete_book_from_form():
    book_id = request.form.get('id')
    book = Book.query.get(book_id)

    if not book:
        flash(f'Buku dengan ID {book_id} tidak ditemukan.', 'danger')
        return redirect(url_for('home'))

    db.session.delete(book)
    db.session.commit()
    flash(f'Buku ID {book_id} berhasil dihapus!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret123'  # <-- Wajib untuk Flash Message

# Konfigurasi untuk MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/booksmy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Model database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penulis = db.Column(db.String(100), nullable=False)
    judul_buku = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Penulis': self.penulis,
            'Judul Buku': self.judul_buku,
            'Harga': self.harga
        }

# Membuat database pertama kali
with app.app_context():
    db.create_all()
    print("Database berhasil dibuat atau sudah ada.")

# API CRUD

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_data = request.get_json()
    new_book = Book(
        penulis=new_data['Penulis'],
        judul_buku=new_data['Judul Buku'],
        harga=new_data['Harga']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = Book.query.get(book_id)
    if book:
        if 'Penulis' in updated_data:
            book.penulis = updated_data['Penulis']
        if 'Judul Buku' in updated_data:
            book.judul_buku = updated_data['Judul Buku']
        if 'Harga' in updated_data:
            book.harga = updated_data['Harga']
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.to_dict()), 200
    return jsonify({'error': 'Buku Tidak Ditemukan'}), 404

# Halaman Home (GUI)
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Tambahkan Buku dari Form HTML
@app.route('/add_book', methods=['POST'])
def add_book_from_form():
    try:
        penulis = request.form['penulis']
        judul_buku = request.form['judul_buku']
        harga = request.form['harga']
        
        new_book = Book(penulis=penulis, judul_buku=judul_buku, harga=harga)
        db.session.add(new_book)
        db.session.commit()

        flash('Buku berhasil ditambahkan!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Gagal menambahkan buku: {str(e)}', 'danger')

    return redirect(url_for('home'))

# Cari Buku dari Form HTML
@app.route('/get_book', methods=['GET'])
def get_book_from_form():
    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    if book:
        flash(f'Ditemukan: {book.judul_buku} oleh {book.penulis} (Harga: Rp{book.harga})', 'success')
    else:
        flash('Buku tidak ditemukan.', 'danger')

    return redirect(url_for('home'))

# Update Buku dari Form HTML
@app.route('/update_book', methods=['POST'])
def update_book_from_form():
    try:
        book_id = request.form['id']
        penulis = request.form['penulis']
        judul_buku = request.form['judul_buku']
        harga = request.form['harga']

        book = Book.query.get(book_id)
        if book:
            book.penulis = penulis
            book.judul_buku = judul_buku
            book.harga = harga
            db.session.commit()

            flash('Buku berhasil diperbarui!', 'success')
        else:
            flash('Buku tidak ditemukan.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Gagal memperbarui buku: {str(e)}', 'danger')

    return redirect(url_for('home'))

# Hapus Buku dari Form HTML
@app.route('/delete_book', methods=['POST'])
def delete_book_from_form():
    try:
        book_id = request.form['id']
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            flash('Buku berhasil dihapus!', 'success')
        else:
            flash('Buku tidak ditemukan.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'Gagal menghapus buku: {str(e)}', 'danger')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
