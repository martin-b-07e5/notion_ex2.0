# notion_ex2.0
notion_ex2.0

### ✅ Create virtual environment</strong>

$ python -m venv .venv

### ✅ Activate virtualenv

$ source .venv/bin/activate

#### ✅ check

$ pip freeze

### ✅ Install

$ pip install Flask

#### ✅ Check

<pre>
$ pip freeze
blinker==1.6.2
click==8.1.6
Flask==2.3.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
Werkzeug==2.3.6
</pre>

### ✅ Install

$ pip install requests

#### ✅ Check

<pre>
  $ pip freeze 
  blinker==1.6.2
  certifi==2023.7.22
  charset-normalizer==3.2.0
  click==8.1.6
  Flask==2.3.2
  idna==3.4
  itsdangerous==2.1.2
  Jinja2==3.1.2
  MarkupSafe==2.1.3
  requests==2.31.0
  urllib3==2.0.4
  Werkzeug==2.3.6
</pre>

### ✅ requirements.txt

$ pip freeze > requirements.txt

### ✅ (optional) en nuevo entorno » instalar todas dependencias

$ pip install -r requirements.txt

### structure

<pre>
$ tree
.
├── static
│ └── styles.css
├── templates
│ └── index.html
├── app.py
├── config.ini
├── readme.md
└── requirements.txt
</pre>


# execute the app
$ python app.py
