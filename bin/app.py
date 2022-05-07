from flask import Flask, render_template
import matplotlib.pyplot as plt

# from manifesAtData import get_dataframe

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

@app.route('/', methods=['GET'])
def getCapatcha():
    left = [1, 2, 3, 4, 5]
    # heights of bars
    height = [10, 24, 36, 40, 5]
    # labels for bars
    tick_label = ['one', 'two', 'three', 'four', 'five']
    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the y-axis
    plt.ylabel('y - axis')
    # naming the x-axis
    plt.xlabel('x - axis')
    # plot title
    plt.title('My bar chart!')

    plt.savefig('static/image/out.png')
    return render_template(
    "index.html"
    )

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
