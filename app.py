from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_rpo(backup_frequency_minutes):
    return backup_frequency_minutes

def calculate_rto(data_size_gb, bandwidth_mbps):
    data_size_gb = float(data_size_gb)
    bandwidth_mbps = float(bandwidth_mbps)
    bandwidth_gbps = bandwidth_mbps / 8 / 1024
    restore_time_seconds = data_size_gb / bandwidth_gbps
    return restore_time_seconds / 3600

@app.route("/", methods=["GET", "POST"])
def index():
    rpo = None
    rto = None
    if request.method == "POST":
        backup_frequency = request.form.get("backup_frequency")
        data_size = request.form.get("data_size")
        bandwidth = request.form.get("bandwidth")
        
        rpo = calculate_rpo(backup_frequency)
        rto = calculate_rto(data_size, bandwidth)
    
    return render_template("index.html", rpo=rpo, rto=rto)

if __name__ == "__main__":
    app.run(debug=True)