# Product Recommendation

# 🛒 Product Recommendation System

A simple **Product Recommendation System** web app built with **Streamlit** that recommends similar products based on their descriptions using natural language processing techniques.

---

## Features

- Search and select products from a dropdown list
- View a list of similar products based on text similarity of product descriptions
- Built with Python, pandas, scikit-learn, and Streamlit
- Data is dynamically loaded from a CSV hosted on Google Drive

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/dishitasood/product_recommendation.git
   cd product_recommendation

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

#Usage

1. Run the Streamlit app locally:

```bash
streamlit run app.py
```
#Data Source

The product data is loaded dynamically from a CSV file hosted on Google Drive. You can update the data by replacing the CSV and updating the file ID in main.py.

#Technologies Used
Python 3

Streamlit

pandas

scikit-learn (TF-IDF and cosine similarity)

Google Drive (for dataset hosting)

#Contributing
Feel free to open issues or submit pull requests to improve the app.





  

   


