import streamlit as st
from PIL import Image

# Set up page config
st.set_page_config(page_title="Py Auto Solutions", layout="wide")

# Load the logo image
logo_path = "images/py_auto_solutions_logo.png"
try:
    logo = Image.open(logo_path)
    st.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error("Logo image not found. Make sure the path is correct.")

# Navigation
menu = ["Home", "Services", "Blog", "Pricing", "Contact Us"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.title("Welcome to Py Auto Solutions")
    st.write("""
    At Py Auto Solutions, we specialize in leveraging artificial intelligence and automation technologies to transform your business operations. Our mission is to empower businesses with cutting-edge AI solutions, comprehensive data analysis, and tailored professional services to drive growth and efficiency.
    """)

# Services Page
elif choice == "Services":
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

# Blog Page
elif choice == "Blog":
    st.title("Our Blog")
    st.write("Coming soon! Stay tuned for insights and updates from the world of AI and business automation.")

# Pricing Page
elif choice == "Pricing":
    st.title("Pricing")
    st.write("We offer competitive pricing for our services. Contact us for a customized quote based on your specific needs.")

# Contact Us Page
elif choice == "Contact Us":
    st.title("Contact Us")
    st.write("Get in touch with us for more information about our services or to request a quote.")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write("Thank you for getting in touch! We will respond to your message as soon as possible.")
            # Here you can add code to send the message to your email or save it to a database

# Payment with Paystack
def process_payment():
    st.subheader("Make a Payment")
    email = st.text_input("Email")
    amount = st.number_input("Amount", min_value=0)
    if st.button("Pay"):
        headers = {
            "Authorization": "Bearer YOUR_PAYSTACK_SECRET_KEY",
            "Content-Type": "application/json"
        }
        data = {
            "email": email,
            "amount": int(amount * 100)  # Paystack works with the smallest currency unit
        }
        response = requests.post("https://api.paystack.co/transaction/initialize", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            payment_url = response.json()['data']['authorization_url']
            st.write(f"Click [here]({payment_url}) to complete your payment.")
        else:
            st.write("Error initializing payment. Please try again.")

# Add a sidebar option for payment
st.sidebar.subheader("Payment")
process_payment()

