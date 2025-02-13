from flask import Flask, render_template, request
from rules import infer_heart_disease

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = None
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")  # Lấy danh sách triệu chứng từ form
        diagnosis = infer_heart_disease(set(symptoms))  # Gửi vào hệ thống suy diễn
    return render_template("index.html", diagnosis=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)
