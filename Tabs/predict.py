"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Alzheimer's Detection.
            </p>
        """, unsafe_allow_html=True)

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Response", int(df["Response"].min()), int(df["Response"].max()))
    B = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    C= st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    D = st.slider("Peripheral Nervous System Activity Scale", int(df["PNSA"].min()), int(df["PNSA"].max()))
    E = st.slider("SES", int(df["SES"].min()), int(df["SES"].max()))
    F = st.slider("MMSE", int(df["MMSE"].min()), int(df["MMSE"].max()))
    G = st.slider("CDR", int(df["CDR"].min()), int(df["CDR"].max()))
    H = st.slider("eTIV", int(df["eTIV"].min()), int(df["eTIV"].max()))
    I = st.slider("nWBV", float(df["nWBV"].min()), float(df["nWBV"].max()))
    J = st.slider("ASF",int(df["ASF"].min()), int(df["ASF"].max()))
    K = st.slider("Group",int(df["Group"].min()), int(df["Group"].max()))
    
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to regular forgetfulness")
        elif (prediction == 2):
            st.warning("The person is prone to mild Alzhiemer")
        elif (prediction == 3):
            st.warning("The person is prone to clinical Alzhiemer")
        elif (prediction == 4):
            st.warning("The person is prone to chronic Alzhiemer")
        elif (prediction == 5):
            st.warning("The person is prone to severe Alzhiemer")
        else:
            st.success("The person has no Alzheimer")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
