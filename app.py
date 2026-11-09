
import streamlit as st
import pandas as pd

from src.analyzer import inspect_dataset, data_quality_report

from src.visualizer import (
    plot_histogram,
    plot_boxplot,
    plot_bar_chart,
    plot_correlation_heatmap
)


st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="📊",
    layout="wide"
)

st.title("ResearchPilot AI")
st.write("Explore, analyse and understand your datasets.")

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)


if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        if df.empty:
            st.warning("The uploaded dataset is empty.")
            st.stop()

        inspection = inspect_dataset(df)
        quality = data_quality_report(df)

        st.success("Dataset uploaded successfully!")

        # Dataset overview
        st.header("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Rows", inspection["rows"])
        col2.metric("Total Columns", inspection["columns_count"])
        col3.metric("Duplicate Rows", quality["duplicate_rows"])

        # Dataset preview
        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Analysis sections
        tab1, tab2, tab3, tab4 = st.tabs([
            "Data Information",
            "Data Quality",
            "Visualizations",
            "Dataset Summary"
        ])

        with tab1:
            st.subheader("Column Information")

            column_info = pd.DataFrame({
                "Data Type": inspection["data_types"],
                "Missing Values": inspection["missing_values"],
                "Missing Percentage": inspection["missing_percentage"]
            })

            st.dataframe(column_info, use_container_width=True)

            st.write("Numerical Columns")
            st.write(inspection["numerical_columns"])

            st.write("Categorical Columns")
            st.write(inspection["categorical_columns"])

        with tab2:
            st.subheader("Data Quality Report")

            quality_table = pd.DataFrame({
                "Missing Values": quality["missing_values"],
                "Missing Percentage": quality["missing_percentage"],
                "Unique Values": quality["unique_values"]
            })

            st.dataframe(quality_table, use_container_width=True)

            st.write("Constant Columns")
            st.write(quality["constant_columns"])

        with tab3:
            st.subheader("Explore Your Data")

            chart_type = st.selectbox(
                "Choose a visualization",
                [
                    "Histogram",
                    "Box Plot",
                    "Bar Chart",
                    "Correlation Heatmap"
                ]
            )

            if chart_type == "Histogram":
                columns = inspection["numerical_columns"]

                if columns:
                    column = st.selectbox("Select a column", columns)
                    fig = plot_histogram(df, column)
                    st.pyplot(fig)
                else:
                    st.info("No numerical columns available.")

            elif chart_type == "Box Plot":
                columns = inspection["numerical_columns"]

                if columns:
                    column = st.selectbox("Select a column", columns)
                    fig = plot_boxplot(df, column)
                    st.pyplot(fig)
                else:
                    st.info("No numerical columns available.")

            elif chart_type == "Bar Chart":
                columns = inspection["categorical_columns"]

                if columns:
                    column = st.selectbox("Select a column", columns)
                    fig = plot_bar_chart(df, column)
                    st.pyplot(fig)
                else:
                    st.info("No categorical columns available.")

            elif chart_type == "Correlation Heatmap":
                fig = plot_correlation_heatmap(df)

                if fig is not None:
                    st.pyplot(fig)
                else:
                    st.info(
                        "At least two numerical columns are required."
                    )

        with tab4:
            st.subheader("Automatic Dataset Summary")

            st.write(
                f"The dataset contains {inspection['rows']} rows "
                f"and {inspection['columns_count']} columns."
            )

            st.write(
                f"It contains {len(inspection['numerical_columns'])} "
                "numerical columns and "
                f"{len(inspection['categorical_columns'])} "
                "categorical columns."
            )

            total_missing = sum(quality["missing_values"].values())

            st.write(
                f"There are {total_missing} missing values "
                f"and {quality['duplicate_rows']} duplicate rows."
            )

            st.write("Statistical Summary")

            summary_df = pd.DataFrame(
                inspection["summary"]
            ).T

            st.dataframe(summary_df, use_container_width=True)

    except Exception as e:
        st.error(f"Unable to analyse the dataset: {e}")

else:
    st.info("Upload a CSV file to begin your analysis.")
