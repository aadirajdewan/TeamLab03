import streamlit as st

st.title("Aadi's Info")
st.write("""
This page contains a detailed template describing Aadi Raj Dewan's experience, internships, skills, 
and educational background.
""")

profile_picture = "profile 2.jpg"
about_me = "Hi I am Aadi Raj Dewan. I am currently pursing my Bachelor's Degree in Industrial Engineering at Georgia Institute of Technology. I hope to leave Georgia Tech with a full-time offer for consulting in the field of finance."


linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

my_linkedin_url = "https://www.linkedin.com/in/aadirajdewan/"
my_github_url = "https://github.com/aadirajdewan"
my_email_address = "aadird13@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Industrial Engineering (minor in CS)',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': '2028',
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "CS 1331", "MATH 1553", "CS 2063"], 
    "names":["Intro to Computing in Python", "Intro to OOP", "Intro to Linear Algebra", "Intro to Discrete Mathematics"], 
    "semester_taken":["Fall 2024", "Spring 2025", "Spring 2025", "Spring 2025"],
    "skills":["Python Data Structures - tuples, dicts, lists, str", "OOP in Java and the application of classes", "Classes, Eigenvalues, Determinants", "Induction, Diagonalization, Proofs"],
    }
experience_data = {
  "Research Intern at IIT (Indian Institute of Technology)": ([
    "- Studied ongoing research on the mathematical modeling of ecological ecosystems, focusing on grazing systems",
    "- Implemented equation-solving using computational tools including Python, C++, and MATLAB",
    "- Examined dynamic local stable and unstable equilibrium states and summarized findings in a comprehensive report"
], "iit.jpeg", None),

"Intern at Hyundai Motors Dealership": ([
    "- Used Tableau dashboards, Python, and Microsoft Excel for statistical analysis",
    "- Analyzed large data sets to determine employee efficiency and provided insights for bonus allocation",
    "- Gained hands-on experience with tools to drive organizational performance improvements"
], "hyundai.jpg", None),
}

projects_data = {
    "Watchdog - AI-Based Misinformation Detection Tool": (
    "Watchdog: A web-based tool designed to combat misinformation on social media platforms, utilizing cutting-edge AI technologies.\n\n"
    "Unique Features:\n"
    "- AI-Powered Detection: Identifies misleading content on social media using Llama 3 and the Perplexity AI API.\n"
    "- Chrome Extension: Provides users with a seamless browser extension for real-time misinformation detection while browsing.\n"
    "- Sleek UI: Developed a responsive and user-friendly interface using Tailwind CSS, enabling intuitive interaction.\n\n"
    "Technology Stack:\n"
    "- Backend Intelligence: Integrated Llama 3 for natural language understanding to analyze and flag potentially misleading information.\n"
    "- API Utilization: Used the Perplexity AI API for querying and verifying the accuracy of online content.\n"
    "- Frontend Design: Built a sleek and interactive user interface using Tailwind CSS.\n"
    "- Web Scraping: Designed tools for efficient data collection and analysis to streamline misinformation detection."
), "Stock Trader": ("The Stock Tracker app provides real-time analysis of stock price trends using data from the Alpha Vantage API. Users can input stock symbols to retrieve the latest market data, select a date range to visualize historical trends, and analyze specific data points dynamically. The app leverages user interactions like text input, sliders, and dropdowns, along with dynamic visualizations such as line graphs and metrics. It also calculates and displays percentage changes in stock prices over the selected period, making it a powerful tool for stock market enthusiasts and analysts.")

}

programming_data = {
    "Python": 95,
    "Javascript": 50,
    "HTML5 & CSS": 65,
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "HTML5 & CSS": "🔍",
}

spoken_icons = {
    "English": "🇬🇧",
    "Bengali": "🇫🇷",
    "Spanish": "🇪🇸",
    "French": "🇪🇸"
}

spoken_data = {
    "English": "Bilingual Proficiency",
    "Hindi": "Native Proficiency",
    "Spanish": "Limited Working Proficiency",
    "French": "Limited Working Proficiency"
}

leadership_data = {
   "Competitive Chess Player - GT Chess Club (2024 - Present)": [
    "- Represented Georgia Tech in multiple online chess tournaments as part of the inter-collegiate sports league",
    "- Won several local tournaments and achieved a FIDE rating of 1483, with an online rating exceeding 2000 on chess.com",
    "- Actively participated in organizing chess events, promoting strategic thinking and sportsmanship among peers"
]

}

activity_data = {
   "Instrumental Music: Saxophone (January 2018 - Present)": [
    "- Represented the NCC Directorate as a saxophonist in a marching band during India's Republic Day and the Prime Minister’s Rally in 2020",
    "- Built an online presence by curating saxophone covers and flute reels on Instagram (@aadi.with.the.sax), amassing over 100 followers",
    "- Showcased dedication and artistry by blending music with formal events, reflecting discipline and creative expression"
]

}


