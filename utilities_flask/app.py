from flask import Flask, render_template, request, redirect
import pytube 
from fpdf import FPDF
import pyqrcode
import png
from pyqrcode import QRCode

# Defining App

app = Flask(__name__)
app.debug = True

# Creating Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/video-downloader', methods=['GET','POST'])
def video():
    if (request.method=='POST'):
        url = request.form.get('video_url')
        yt = pytube.YouTube(url)
        yt.streams.first().download()
        return "<script>alert('thanks for using our services')</script>"

        

    return render_template('v_d.html')
    
    


@app.route('/converter', methods=['GET','POST'])
def converter():
    if (request.method=='POST'):
        pdf = FPDF()
        imagelist = request.form.get('images')
        for image in imagelist:
            pdf.add_page()
            pdf.image(image)
            pdf.output("new.pdf","F")

        return "Success"

    return render_template('converter.html')

@app.route('/QR-Code', methods=['GET','POST'])
def qr_code():
    if (request.method=='POST'):
        url = request.form.get("qr_url")
        qr_code = pyqrcode.create(url)
        qr_code.svg("qr_code1.svg", scale=8)
        qr_code.png("qr_code1.png", scale=6)
    
    return render_template('q_r.html')

