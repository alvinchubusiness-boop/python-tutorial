import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 1. Read the Dataset
# 'on_bad_lines' handles formatting errors often found in this specific CSV
df = pd.read_csv('books.csv', on_bad_lines='skip')

# 2. Popularity-based Recommender (IMDB Weighted Rating)
def popularity_recommender(df, n=5):
    C = df['average_rating'].mean()
    m = df['ratings_count'].quantile(0.9)
    q_books = df.copy().loc[df['ratings_count'] >= m]
    
    def weighted_rating(x, m=m, C=C):
        v, R = x['ratings_count'], x['average_rating']
        return (v/(v+m) * R) + (m/(m+v) * C)
        
    q_books['score'] = q_books.apply(weighted_rating, axis=1)
    return q_books.sort_values('score', ascending=False)[['title', 'authors', 'score']].head(n)

# 3. Content-based Recommender (TF-IDF on Authors)
def content_recommender(title, df, n=5):
    # TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['authors'])
    
    # Distance Matrix (Cosine Similarity)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Create mapping of titles to indices
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    
    if title not in indices:
        return "Book not found."
    
    # Get index for the title
    idx = indices[title]
    
    # Handle duplicates by taking the first positional occurrence
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
    
    # Calculate similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    
    book_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[book_indices]

# --- Final Outputs ---
print("--- Top 5 Popular Books (Weighted Rating) ---")
print(popularity_recommender(df))

print("\n--- Recommendations for 'Harry Potter and the Half-Blood Prince' ---")
# Ensure the title matches exactly as it appears in your dataset
search_title = 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)'
print(content_recommender(search_title, df))