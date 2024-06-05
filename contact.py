import streamlit as st

def app():

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")

    # start form page 
    st.title("Contact Me")
    st.write("Feel free to reach out about career oppurtunities, research, or anything else you found interesting on my site.")

    contact_form = """
    <form action="https://formsubmit.co/akanksha@ramabadran.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message"></textarea>
        <button type="submit" class="horizontal-center">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    submit_message = """
    <script>
    document.getElementById('contactForm').addEventListener('submit', function() {
        alert('Thank you for your message!');
    });
    </script>
    """)

    st.markdown(submit_message, unsafe_allow_html=True)
    
