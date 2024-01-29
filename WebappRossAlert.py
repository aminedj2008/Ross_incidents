from cProfile import label
import streamlit as st
import datetime
from datetime import date
import requests

import pickle
from pathlib import Path
import streamlit_authenticator as stauth


from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.set_page_config(layout="wide")




names =["SPS","MSPS"]
usernames = ["SPS","MSPS"]



file_p="https://github.com/aminedj2008/Ross_incidents/blob/main/password_key.pk1"
with file_p.open("rb") as file :
    hash_password = pickle.load(file)

    authenticator = stauth.Authenticate(names, usernames, hash_password,"theftincd","abcdf",cookie_expiry_days=30)

    name,authentication_status,username=authenticator.login("login","main")

    if authentication_status == False:
         st.error("Username/password is incorrect")

    if authentication_status == None:
         st.warning("Please enter your user name and password")
    if authentication_status:     
              


                # Establishing a Google Sheets connection

                webhook="https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY5MDYzZjA0MzQ1MjZmNTUzMzUxM2Ei_pc"

                # Function to post data to the webhook using argument unpacking
                def post_to_webhook(**data):
                    response = requests.post(webhook, json=data)
                    return response



                # List of Business Types and Products
                BUSINESS_TYPES = [
                    "Men shoes",
                    "Men cloths",
                    "Men Basic",
                    "Ladies shoes",
                    "Ladies cloths",
                    "Ladies Basics"
                    "MAkeup",
                    "Jewelry",
                    "Perfume",
                    "Kids cloths",
                    "Kids shoes",
                    "Kids basics",
                    "Home",
                    "Juniors",


                ]
                PRODUCTS = [
                    "Men shoes",
                    "Men cloths",
                    "Men Basic",
                    "Ladies shoes",
                    "Ladies cloths",
                    "Ladies Basics"
                    "MAkeup",
                    "Jewelry",
                    "Perfume",
                    "Kids cloths",
                    "Kids shoes",
                    "Kids basics",
                    "Home",
                    "Juniors",
                ]

                yesno = [
                    "Yes",
                    "No",
                    
                ]




                st.image('ross.png')

                # Establishing a Google Sheets connection
                #conn = st.experimental_connection("gsheets", type=GSheetsConnection)
                #existing_data = conn.read(worksheet="Rosstheftdata", usecols=list(range(6)), ttl=12)




                st.header("The internal reporting systme for Store 0594")

                # Add a new theft incident
                with st.form(key="Theft_form"):
                    store_number = st.text_input(label="Store Number*")
                    d1 = st.selectbox("Department 1*", options=BUSINESS_TYPES, index=None)
                    d2 = st.selectbox("Department 2", options=PRODUCTS , index=None)
                    repeater = st.selectbox("Repeater", options=yesno)
                    
                    theft_date = st.date_input(label="Incident Date")
                    enter_time= st.time_input(label="Entry Time")
                    exite_time= st.time_input(label="Exite Time" )

                    additional_info = st.text_area(label="Subject Discription")

                    # Mark mandatory fields
                    st.markdown("**required*")

                    submit_button = st.form_submit_button(label="Submit Incident Details")

                    # If the submit button is pressed
                    
                if submit_button:
                        if not store_number.strip():
                            st.error("Please enter your store number. 💡")
                            st.stop()

                        data = {"StoreNBR": store_number, "Department 1": d1, "Department 2": d2,"Repeater": repeater,"Theftdate":theft_date.strftime("%Y-%m-%d") ,"Entertime":enter_time.strftime(" %H:%M:%S") ,
                                "Exitetime":exite_time.strftime("%H:%M:%S")  , "Dis":additional_info}
                        response = post_to_webhook(**data)
                        if response.status_code == 200:
                            st.success("Thanks for your submission! 🌟")
                        else:
                            st.error("There was an error. Please try again. 🛠️")


                            import streamlit as st
                from streamlit_gsheets import GSheetsConnection

                url = "https://docs.google.com/spreadsheets/d/1SkgIoTt4AzgJEidTG5i2TvRuMK1HiM0aJ4SdLvSzLCs/edit#gid=0"

                conn = st.experimental_connection("gsheets", type=GSheetsConnection)

                data = conn.read(spreadsheet=url, usecols=list(range(8)))
                st.dataframe(data)

                authenticator.logout("Logout")
