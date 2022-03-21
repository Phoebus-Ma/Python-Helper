###
# Python flask test.
# 
# License - MIT
###

import os
from flask import Flask, request, render_template


# Create flask instance.
flask_app = Flask(__name__)


# Home page.
@flask_app.route('/', methods = ['GET'])
def home():
# {
    return render_template('calculator.html')
# }


# Calculator result.
@flask_app.route('/calclate_result/', methods = ['POST'])
def calclate_result():
# {
    result = None

    # Get user input value.
    input_1 = request.form['Input1']
    input_2 = request.form['Input2']
    operation = request.form['operation']

    try:
        param1 = float(input_1)
        param2 = float(input_2)

        if '+' == operation:
            result = param1 + param2
        elif '-' == operation:
            result = param1 - param2
        elif '/' == operation:
            result = param1 / param2
        else:
            result = param1 * param2
        
        return render_template(
            'calculator.html',
            input1      = param1,
            input2      = param2,
            operation   = operation,
            result      = result,
            calculation_success = True
        )

    except ZeroDivisionError:
        return render_template(
            'calculator.html',
            error = 'Error in division 0.',
            calculation_success = False
        )

    except ValueError:
        return render_template(
            'calculator.html',
            error = 'Error in value.',
            calculation_success = False
        )
# }


# Main function.
def main():
# {
    # Run app.
    flask_app.debug = True
    flask_app.run()
# }


# Program entry.
if '__main__' == __name__:
    main()
