import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Tech Explorer", page_icon=":computer:")

    # Page title and introduction
    st.title('Welcome to Tech Explorer')
    st.write('Explore the latest in technology with us.')

    # About section
    st.header('About')
    st.write('Tech Explorer is your guide to tech news, trends, and innovations.')

    # Key Technologies section
    st.header('Key Technologies')
    st.markdown("""
    - **Artificial Intelligence**: Discover the future of AI and machine learning.
    - **Blockchain**: Explore decentralized technologies and cryptocurrencies.
    - **Internet of Things (IoT)**: Learn about connected devices and smart home technology.
    - **Cloud Computing**: Dive into cloud services and infrastructure.
    """)

    # Featured Articles section
    st.header('Featured Articles')
    st.markdown("""
    - [Understanding Neural Networks](https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/)
    - [Introduction to Blockchain Technology](https://www.geeksforgeeks.org/blockchain-technology-introduction/)
    - [The Role of IoT in Smart Cities](https://bridgera.com/the-role-of-iot-in-smart-city/)
    """)

    # Call to action
    st.header('Get Started')
    st.write('Start exploring the world of technology today.')
    st.write('Feel free to browse our articles and resources.')

    # Contact information
    st.header('Contact Us')
    st.write('For inquiries or feedback, contact us at: ')
    st.write('Email: contact@techexplorer.com')
    st.write('Phone: +1234567890')

if __name__ == '__main__':
    main()
