import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd

def emails_to_dataframe(emails: list, columns_to_preprocess: list) -> pd.DataFrame:
    '''
    Converts a list of dictionaries containing email information into a pandas DataFrame.

    Args:
        emails (list): List of dictionaries, where each dictionary represents an email.

    Returns:
        pd.DataFrame: DataFrame with the email data.
    '''
    data_frame = pd.DataFrame(emails)
    data_frame = clean_dataframe_text(data_frame, columns_to_preprocess)
    data_frame = clear_index_column(data_frame)
    export_data(data = data_frame, path = 'data/emails.csv')
    return data_frame

def export_data(data: pd.DataFrame, path: str) -> None:
    '''
    Export data to a CSV file.

    Args:
        data (pd.DataFrame): DataFrame containing email data.
        path (str): Path to save the CSV file.
    '''
    data.to_csv(path, index=False)

def download_nltk_resources() -> None:
    '''
    Download the necessary NLTK resources for text processing.

    Args:
        None
    '''
    resources = ['punkt', 'stopwords', 'wordnet']
    for resource in resources:
        try:
            nltk.data.find(f'tokenizers/{resource}' if resource == 'punkt' else f'corpora/{resource}')
        except LookupError:
            print(f"Downloading NLTK resource: {resource}...")
            nltk.download(resource)

def preprocess_text(text: str) -> str:
    '''
    Lemmatizes and removes stopwords from the input text.
    
    Args:
        text (str): Input text to be preprocessed.
    
    Returns:
        str: Preprocessed text.
    '''
    if pd.isnull(text):
        return text
    download_nltk_resources()
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_tokens = [
        lemmatizer.lemmatize(word) 
        for word in tokens 
        if word.isalpha() and word not in stop_words 
    ]
    return ' '.join(processed_tokens)

def clean_dataframe_text(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    '''
    Preprocess text data in specified columns of a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing text data.
        columns (list): List of column names to preprocess.
    
    Returns:
        pd.DataFrame: DataFrame with preprocessed text data.
    '''
    download_nltk_resources()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].apply(preprocess_text)
    return df

def clear_index_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Convert the index column to integer type.

    Args:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame with index column converted to integer type.
    '''
    df['id'] = df['id'].astype(int)
    return df


