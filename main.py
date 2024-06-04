import math

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    value = None

    if request.method == 'POST':
        try:
            precision = request.form.get('precision')

            if not precision:
                precision = 2
            else:
                if precision == -0:
                    precision = 0;

                precision = abs(int(precision))
            x = float(request.form.get('x'))

            function = request.form.get("function")
            measure = request.form.get("measure")

            if measure == "Градусы":
                x = math.radians(x)


            if function:
                if function == "sinx":
                    value = round(math.sin(x), precision)
                elif function == "cosx":
                    value = round(math.cos(x), precision)
                elif function == "tgx":
                    value = round(math.tan(x), precision)
                elif function == "ctgx":
                    value = round((1/math.tan(x)), precision)
        except(ValueError, TypeError):
            value = "Ошибка ввода"
    return render_template("index.html", value=value)

if __name__ == "__main__":
    app.run(debug=True)