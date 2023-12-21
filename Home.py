import streamlit as st

def main():
    st.set_page_config(page_title="Elijah", page_icon="")


    st.title("Elijah Wandimi")

    st.subheader("Data engineer | Data analyst | Machine learning engineer")

    st.subheader("About")
    st.markdown("""
                Experienced data engineer with a passion for deep learning.
                """)

    st.header("Skills")
    st.markdown("""
                Languages: Python, Java, SQL

                Storage: Snowflake, MySQL, PostgresSQL, BigQuery

                Tools: DBT, Looker, Tableau, Excel, GCP, AWS, Azure, Kafka, Airflow, Spark

                Other: statistical modelling, A/B testing, deep learning, ETL/ELT processes
                """)
    
    st.header("Education")
    st.subheader("Software engineering  - Multimedia University of Kenya, Bsc")
    st.markdown("""
                Focus in mathematics (linear algebra, calculus, statistics & probability), machine learning, database and distributed systems,
                statistical data analysis, systems engineering
                """)



if __name__ == "__main__":
    main()