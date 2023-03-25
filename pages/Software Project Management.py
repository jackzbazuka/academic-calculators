import numpy as np
import pandas as pd
import streamlit as st

with st.expander("Function Point Analysis"):
    st.write(
        "Function Point Analysis was initially developed by Allan J. Albercht in 1979 at IBM and it has been further modified by the International Function Point Users Group (IFPUG). FPA provides a standardized method to functionally size the software work product."
    )

    col1, col2, col3 = st.columns(3)

    df = pd.DataFrame(
        np.zeros((5, 3)),
        columns=["Simple", "Average", "Complex"],
        index=[
            "External Inputs",
            "External Outputs",
            "External Enquiry",
            "Internal Files",
            "External Interface Files",
        ],
    )

    with col1:
        external_input = st.number_input(
            "External Inputs",
            min_value=0,
            max_value=100,
            value=0,
            help="Functions related to data entering the system",
        )
        internal_files = st.number_input(
            "Internal Files",
            min_value=0,
            max_value=100,
            value=0,
            help="Logical files maintained within the system. Log files are not included here.",
        )
        total_degree_of_influence = st.number_input(
            "Total Degree of Influence",
            min_value=0,
            max_value=70,
            value=0,
            help="Sum of each of 14 influential factors. Ranging from 0-5.",
        )

    with col2:
        external_output = st.number_input(
            "External Outputs",
            min_value=0,
            max_value=100,
            value=0,
            help="Functions related to data exiting the system.",
        )
        external_interface_files = st.number_input(
            "External Interface Files",
            min_value=0,
            max_value=100,
            value=0,
            help="These are logical files for other applications which are used by our system.",
        )

    with col3:
        external_inquiry = st.number_input(
            "External Enquiry",
            min_value=0,
            max_value=100,
            value=0,
            help="They lead to data retrieval from the system but don’t change the system.",
        )
        project_type = st.selectbox(
            "Project Type",
            ("Simple", "Average", "Complex"),
            index=0,
            help="Simple: The project is small and has a short development time. Average: The project is medium in size and has a medium development time. Complex: The project is large and has a long development time.",
        )

    edited_df = st.experimental_data_editor(df, use_container_width=True)

    if st.button("Calculate"):
        input_arr = np.array(
            [
                external_input,
                external_output,
                external_inquiry,
                internal_files,
                external_interface_files,
            ]
        )

        vaf = 0.65 + 0.01 * total_degree_of_influence

        ufp = np.sum(np.multiply(input_arr, edited_df[f"{project_type}"]))

        fpc = ufp * vaf

        st.write(f"VAF: {vaf}")
        st.write(f"UFP: {ufp}")
        st.write(f"FPC: {fpc}")

with st.expander("COCOMO Model"):
    pass

