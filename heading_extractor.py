import pandas as pd
import advertools as adv
import streamlit as st

st.title("""Heading Extractor""")
st.subheader("Upload the CSV File")
# st.write('Download Sample File Below')
href4 = f'<a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vTRHGu1jTiikba2PPVxis1OevUSvaUIp5pfeLXpsSw7r_Bq0Ru_jJvE63-kdlQ_8XXrNFRDdvJP7lbX/pub?gid=0&single=true&output=csv">Download Sample File</a>'
st.markdown(href4, unsafe_allow_html=True)

file = st.file_uploader('',type='csv')
try:
    url_df = pd.read_csv(file)
    url_list = url_df['url'].values.tolist()

    adv.crawl(url_list, output_file='vedantu_data1.jl', follow_links=False)
    crawl_df = pd.read_json('vedantu_data1.jl', lines=True)
    heading_df = crawl_df[['url','h2','h3']]
    print(heading_df)
    st.write(heading_df)
    st.success("Done!") 

    csv = heading_df.to_csv(index=False)

    st.download_button('Download CSV', csv, 'heading_data.csv', 'text/csv')

except:
    print('Error')
