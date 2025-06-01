import pandas as pd

file_id = '1Pmo2YBIeaKcFe_OXuqeGfb-zwvoBkdOp'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url)

df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

df = df[df['CustomerID'].notna()]

user_item = df.pivot_table(index='CustomerID', columns='StockCode', values='Quantity', aggfunc='sum', fill_value=0)

df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]

df['Description'] = (
    df['Description'].fillna('').str.lower()
    .str.replace('[^a-zA-Z ]', '', regex=True)
    .str.strip()
)

product_preview = (
    df[['StockCode', 'Description']]
    .drop_duplicates(subset=['StockCode'])
    .reset_index(drop=True)
)

from sklearn.feature_extraction.text import TfidfVectorizer

#%%
#initialize the vectorizer
tfidf = TfidfVectorizer(stop_words='english')

#fit and transform the product description
tfiidf_matrix = tfidf.fit_transform(product_preview['Description'])
#%%
from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity(tfiidf_matrix)

from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity(tfiidf_matrix)

def Product_Recommender(product_index, top_n=5):
    sim_scores = list(enumerate(similarity_matrix[product_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommended_indices = [i[0] for i in sim_scores]
    return df.iloc[recommended_indices]
#%%
print("Product:", product_preview.iloc[10]['Description'])
print("\nRecommended:")
print(Product_Recommender(10))
