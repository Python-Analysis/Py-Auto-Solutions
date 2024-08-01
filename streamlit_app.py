import streamlit as st
from PIL import Image
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up page config
st.set_page_config(page_title="Py Auto Solutions", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f4;
        color: #333;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #007bff;
        color: white;
        border-bottom: 2px solid #0056b3;
    }
    .header img {
        height: 60px;
    }
    .nav {
        display: flex;
        list-style-type: none;
        margin: 0;
        padding: 0;
    }
    .nav li {
        margin-right: 20px;
    }
    .nav li a {
        text-decoration: none;
        color: white;
        font-weight: bold;
    }
    .nav li a:hover {
        color: #f0f0f0;
    }
    .container {
        padding: 20px;
    }
    .section-title {
        font-size: 24px;
        color: #007bff;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 20px;
        background-color: #007bff;
        color: white;
        border-top: 2px solid #0056b3;
    }
    .review {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        background-color: #fff;
    }
    .review img {
        border-radius: 50%;
        width: 50px;
        height: 50px;
        vertical-align: middle;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load the logo image
logo_path = "C:/Users/Raymond Onwude/.anaconda/app.py/py_auto_solutions_logo.png"
try:
    logo = Image.open(logo_path)
except FileNotFoundError:
    st.error("Logo image not found. Make sure the path is correct.")

# Header
st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{st.image(logo, use_column_width=False)}" class="logo">
        <ul class="nav">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#blog">Blog</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#contact">Contact Us</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Home Page
st.markdown("<a name='home'></a>", unsafe_allow_html=True)
st.title("Welcome to Py Auto Solutions")
st.write("""
At Py Auto Solutions, we are committed to transforming your business operations with cutting-edge AI and automation technologies. Our mission is to empower businesses by leveraging state-of-the-art solutions, comprehensive data analysis, and tailored professional services to drive efficiency and growth.

With a track record of excellence across multiple continents, we deliver solutions that are both innovative and effective. Whether you're looking to optimize processes, enhance your financial performance, or achieve compliance, we have the expertise to help you succeed.
""")

# About Us Section
st.markdown("<a name='about'></a>", unsafe_allow_html=True)
st.subheader("About Us")
st.write("""
Founded with a vision to revolutionize business operations, Py Auto Solutions is at the forefront of AI and automation. Led by Raymond Okhia Onwude, who brings a wealth of experience from diverse global markets, we are dedicated to delivering tailored solutions that meet the unique needs of each client.

Our commitment to excellence and client satisfaction has earned us a solid reputation in the industry. We’ve empowered businesses across Nigeria, Australia, and Malaysia to optimize their operations, improve financial performance, and maintain compliance.
""")

# Services Section
st.markdown("<a name='services'></a>", unsafe_allow_html=True)
st.subheader("Our Services")
st.write("""
- **SEO Optimization and Professional Brand Management**: Boost your online presence and brand visibility with our expert SEO and brand management services.
- **Data Analysis and Visualization**: Extract valuable insights from your data through advanced analytics and visualization techniques.
- **Customized Automation of Business Processes**:
    - Bulk Mailing and Messaging
    - Excel Optimization for Business Efficiency
    - Financial Modeling and Tax Return Filing
    - Business Registration and Compliance
    - Comprehensive Financial Auditing
    - Website Development and Maintenance
- **Consulting and Support**: Receive personalized advice and support to drive your business success with our consulting services.
""")

# Blog Page
st.markdown("<a name='blog'></a>", unsafe_allow_html=True)
st.subheader("Our Blog")
st.write("Stay tuned for insights and updates from the world of AI and business automation.")

# Pricing Page
st.markdown("<a name='pricing'></a>", unsafe_allow_html=True)
st.subheader("Pricing")
st.write("Our pricing is designed to be competitive and transparent. Contact us to get a customized quote based on your specific needs.")
if st.button("Request a Quote"):
    email = st.text_input("Email")
    amount = st.number_input("Amount", min_value=0)
    if st.button("Submit"):
        st.write("Thank you for your interest! We will get back to you shortly with a customized quote.")
        # Placeholder for email or further processing

# Contact Us Page
st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
st.subheader("Contact Us")
st.write("We’re here to assist you. Reach out to us for more information about our services or to request a quote.")

with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write("Thank you for reaching out! We will respond to your message as soon as possible.")
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = "ray_zion@yahoo.com"
        msg['Subject'] = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("your_email@gmail.com", "your_email_password")
            text = msg.as_string()
            server.sendmail(email, "ray_zion@yahoo.com", text)
            server.quit()
            st.success("Message sent successfully")
        except:
            st.error("Failed to send message. Please try again later.")

# Client Reviews Section
st.markdown("<a name='reviews'></a>", unsafe_allow_html=True)
st.subheader("Client Reviews")
st.write("""
### Nigeria
<div class="review">
    <img src="https://via.placeholder.com/50" alt="Client Photo">
    <strong>Chinedu Obi</strong><br>
    "Py Auto Solutions provided exceptional service and transformed our financial processes. Their expertise and attention to detail were second to none."
</div>

### Australia
<div class="review">
    <img src="https://via.placeholder.com/50" alt="Client Photo">
    <strong>Emma Johnson</strong><br>
    "The team at Py Auto Solutions delivered top-notch solutions for our data analysis needs. Their professionalism and innovative approach were impressive."
</div>

### Malaysia
<div class="review">
    <img src="https://via.placeholder.com/50" alt="Client Photo">
    <strong>Ahmad Rizal</strong><br>
    "We are extremely satisfied with the automation services provided by Py Auto Solutions. They helped us streamline operations and improve efficiency significantly."
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Py Auto Solutions. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
