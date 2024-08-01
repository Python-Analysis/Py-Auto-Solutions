import streamlit as st
from PIL import Image
import requests
import json



# Load the logo image
logo_path = "C:/Users/Raymond Onwude/.anaconda/app.py/py.auto.solutions.logo.png"
logo = Image.open(logo_path)

# Set up page config
st.set_page_config(page_title="Py Auto Solutions", page_icon=logo, layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #f8f9fa;
    }
    .header img {
        height: 60px;
    }
    .header nav {
        display: flex;
        gap: 15px;
    }
    .header nav a {
        text-decoration: none;
        color: #333;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 4px;
    }
    .header nav a:hover {
        background-color: #007bff;
        color: #fff;
    }
    .container {
        padding: 20px;
    }
    .footer {
        padding: 20px;
        text-align: center;
        background-color: #f8f9fa;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header with logo and navigation
st.markdown(
    """
    <div class="header">
        <img src="{}" alt="Py Auto Solutions Logo">
        <nav>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#blog">Blog</a>
            <a href="#pricing">Pricing</a>
            <a href="#contact-us">Contact Us</a>
        </nav>
    </div>
    """.format(logo_path),
    unsafe_allow_html=True,
)

# Home Page Content
st.markdown('<div id="home" class="container">', unsafe_allow_html=True)
st.title("Welcome to Py Auto Solutions")
st.write("""
At Py Auto Solutions, we specialize in leveraging artificial intelligence and automation technologies to transform your business operations. Our mission is to empower businesses with cutting-edge AI solutions, comprehensive data analysis, and tailored professional services to drive growth and efficiency.
""")
st.write("### Our Story")
st.write("""
Py Auto Solutions was founded with a vision to revolutionize business operations through AI and automation. With a presence in Asia, Australia, and Nigeria, we have helped numerous clients streamline their processes, increase efficiency, and drive growth. Our team of experts brings a wealth of experience and a passion for innovation to every project.
""")
st.write("### Clients We've Helped")
st.write("""
- A leading e-commerce company in Asia
- A financial services firm in Australia
- A manufacturing company in Nigeria
""")
st.markdown('</div>', unsafe_allow_html=True)

# Services Content
st.markdown('<div id="services" class="container">', unsafe_allow_html=True)
st.title("Our Services")
st.subheader("SEO Optimization and Professional Brand Management")
st.write("Enhance your online presence and brand visibility with our expert SEO and brand management services.")
st.subheader("Data Analysis and Visualization")
st.write("Gain valuable insights from your data through advanced analytics and visualization techniques.")
st.subheader("Customized Automation of Business Processes")
st.write("""
- Bulk Mailing and Messaging
- Excel Optimization for Business Efficiency
- Financial Modeling and Tax Return Filing
- Business Registration and Compliance
- Comprehensive Financial Auditing
- Website Development and Maintenance
""")
st.subheader("Consulting and Support")
st.write("Receive tailored advice and support to drive your business success with our consulting services.")
st.markdown('</div>', unsafe_allow_html=True)

# Blog Content
st.markdown('<div id="blog" class="container">', unsafe_allow_html=True)
st.title("Our Blog")
st.write("Coming soon! Stay tuned for insights and updates from the world of AI and business automation.")
st.markdown('</div>', unsafe_allow_html=True)

# Pricing Content
st.markdown('<div id="pricing" class="container">', unsafe_allow_html=True)
st.title("Pricing")
st.write("We offer competitive pricing for our services. Contact us for a customized quote based on your specific needs.")
# Add a button for payment
if st.button('Make Payment'):
    st.write("Payment functionality coming soon!")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Us Content
st.markdown('<div id="contact-us" class="container">', unsafe_allow_html=True)
st.title("Contact Us")
st.write("Get in touch with us for more information about our services or to request a quote.")
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write("Thank you for getting in touch! We will respond to your message as soon as possible.")
        # Here you can add code to send the message to your email
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        &copy; 2024 Py Auto Solutions. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
