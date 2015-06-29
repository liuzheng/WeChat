# WeChat
Before you RUN Please install Chrome and Chrome-Plugin [gooreplacer4chrome](https://github.com/liuzheng712/gooreplacer4chrome)

Then Start Chrome with the switch `--allow-running-insecure-content`

When you installed gooreplace4chrome plugin , Redirect the `.*webwxApp.*js` to
`http://localhost:8000/js/webwxApp269d63.js` or if you don't want allow chrome running insecure redirect to `https://www.ilz.me/webwxApp269d63.js`,
this js will not update ontime

# How to start this web engine
make sure you have installed python-pip

upgrade pip

    pip install pip -U

install requirements

    pip install -r requirements.txt

run!

    python manage.py runserver

