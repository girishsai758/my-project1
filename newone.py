import streamlit as st
import pandas as pd
from datetime import date
import os



# Initialize or load Excel file
EXCEL_FILE1 = "manpower_data.xlsx"
EXCEL_FILE = "user_data.xlsx"
# Initial data
initial_data = [
    ['ajay', 'supervisior'],
    ['najeeb', 'supervisior'],
    ['ashok', 'skilled'],
    ['ruplal', 'skilled'],
    ['samaru', 'semiskilled'],
    ['rakesh', 'semiskilled']
]

# Create DataFrame and Excel file if not exists
if not os.path.exists(EXCEL_FILE1):
    man_power = pd.DataFrame(initial_data, columns=['name', 'type of work'])
    man_power.to_excel(EXCEL_FILE1, index=False)
else:
    man_power = pd.read_excel(EXCEL_FILE1)
#intializing header columns


data1= ['none','upload data','download data','create list','delete list']
data2=['none','skilled','semiskilled','unskilled','supervisior']


# sidebar configuration
#st.sidebar.header('attendance form')
option1 =st.sidebar.selectbox('select an option',data1)
option2 = st.sidebar.selectbox('select a option',data2)
# download data
if (option1=='download data'):
    option3= st.sidebar.selectbox('select a option',['none','according to person','according to date','according to job'])
    data3 = (man_power[man_power['type of work'] == option2]['name'].tolist())
    read_data = pd.read_excel(EXCEL_FILE)
    # to display according to person
    if (option3=='according to person'):
        st.set_page_config(page_title="Data Collector", layout="centered")
        st.title("📝 Data display Form")
        with st.form("data_display"):
        # User inputs
         name = st.selectbox('select  manpower', data3)
         start_date = st.date_input("starting date of work", min_value=date(1900, 1, 1))
         start_date_string = start_date.strftime("%Y-%m-%d")
         end_date = st.date_input("end date of work", min_value=date(1900, 1, 1))
         end_date_string = end_date.strftime("%Y-%m-%d")
        #submit button
         submitted = st.form_submit_button("display", type="primary")
        # to ensure all required fields are filled
         required_fields = [name,start_date,end_date]
         all_filled = all(required_fields)
         if submitted:
            if not all_filled:
                st.error("Please fill all required fields (*)")
            else:
             read_data = read_data[read_data['Name'] == name]
             read_data = read_data[(read_data['work date']>=start_date_string) &(read_data['work date']<=end_date_string)]
             st.dataframe(read_data[['Name','type of work','work date']])
    #According to job
    if (option3=='according to date'):
        st.set_page_config(page_title="Data Collector", layout="centered")
        st.title("📝 Data display Form")
        # reading excel file
        read_data = pd.read_excel(EXCEL_FILE)
        #form input
        with st.form("data_display"):
            #data input

            start_date = st.date_input("starting date of work", min_value=date(1900, 1, 1))
            start_date_string = start_date.strftime("%Y-%m-%d")
            end_date = st.date_input("end date of work", min_value=date(1900, 1, 1))
            end_date_string = end_date.strftime("%Y-%m-%d")
            # submit button
            submitted = st.form_submit_button("display", type="primary")
            # to ensure all required fields are filled
            required_fields = [start_date, end_date]
            all_filled = all(required_fields)
            if submitted:
                if not all_filled:
                    st.error("Please fill all required fields (*)")
                else:
                    read_data = read_data[(read_data['work date'] >= start_date_string) & (read_data['work date'] <= end_date_string)]
                    st.dataframe(read_data[['Name', 'type of work', 'work date']])
    if (option3=='according to job'):
        st.set_page_config(page_title="Data Collector", layout="centered")
        st.title("📝 Data display Form")
        # reading excel file
        read_data = pd.read_excel(EXCEL_FILE)
        # form input
        with st.form("data_display"):
            # data input
            criteria1 = st.selectbox('select a criteria', ['none','general', 'shift', 'dry','total work force'])
            start_date = st.date_input("starting date of work", min_value=date(1900, 1, 1))
            start_date_string = start_date.strftime("%Y-%m-%d")
            end_date = st.date_input("end date of work", min_value=date(1900, 1, 1))
            end_date_string = end_date.strftime("%Y-%m-%d")
            # submit button
            submitted = st.form_submit_button("display", type="primary")
            # to ensure all required fields are filled
            required_fields = [start_date, end_date]
            all_filled = all(required_fields)
            if submitted:
                if not all_filled:
                    st.error("Please fill all required fields (*)")
                else:
                  if criteria1 == 'general':
                   read_data = read_data[(read_data['type of work']== 'general') | (read_data ['type of work']=='job')]
                   read_data = read_data[(read_data['work date'] >= start_date_string) & (read_data['work date'] <= end_date_string)]
                   read_data= read_data.groupby('skill')['skill'].count()
                   st.table(read_data.to_frame())
                  if criteria1 == 'dry':
                      #count dry persons
                      read_data = read_data[(read_data['type of work'] == 'dry')]
                      read_data = read_data[(read_data['work date'] >= start_date_string) & (read_data['work date'] <= end_date_string)]
                      read_data = read_data.groupby('skill')['skill'].count()
                      st.table(read_data.to_frame())
                  if criteria1 == 'shift':
                      #count morning, evening, night persons
                      read_data = read_data[(read_data['type of work'] == 'morning')|(read_data['type of work'] == 'evening')|(read_data['type of work'] == 'night')]
                      read_data = read_data[(read_data['work date'] >= start_date_string) & (read_data['work date'] <= end_date_string)]
                      read_data = read_data.groupby('skill')['skill'].count()
                      st.table(read_data.to_frame())
                  if criteria1 == 'total work force':
                      # count all persons
                      read_data = read_data[(read_data['work date'] >= start_date_string) & (read_data['work date'] <= end_date_string)]
                      read_data = read_data.groupby('skill')['skill'].count()
                      st.table(read_data.to_frame())



# upload data
if (option1=='upload data'):
    data3 = (man_power[man_power['type of work'] == option2]['name'].tolist())
    # Page configuration
    st.set_page_config(page_title="Data Collector", layout="centered")
    st.title("📝 Data Collection Form")
    with st.form("data_collection"):
# User inputs
     name = st.selectbox('select  manpower',data3)
     type_of_work = st.selectbox('select type of shift',['none','job','morning','evening','night','dry','general'])
     work_date = st.date_input("date of work", min_value=date(1900, 1, 1))

     submitted = st.form_submit_button("Save to Excel", type="primary")
     required_fields = [name, type_of_work]
     all_filled = all(required_fields)
     # Submit button
     if submitted:
        if not all_filled:
            st.error("Please fill all required fields (*)")
        else:
            # Create data dictionary
            new_data = {
                "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "type of work": type_of_work,
                "work date": work_date.strftime("%Y-%m-%d"),
                "skill" : option2,
               # "Experience (years)": experience,
               # "Role": role,
               # "Message": message
            }

            # Create DataFrame
            new_row = pd.DataFrame([new_data])

            # Save to Excel
            if os.path.exists(EXCEL_FILE):
                # Append to existing file
                existing_data = pd.read_excel(EXCEL_FILE)
                updated_data = pd.concat([existing_data, new_row], ignore_index=True)
                updated_data.to_excel(EXCEL_FILE, index=False)
            else:
                # Create new file
                new_row.to_excel(EXCEL_FILE, index=False)

            st.success("Data saved successfully!")
            st.balloons()

# Show existing data
if os.path.exists(EXCEL_FILE):
    st.divider()
    st.subheader("Saved Data Preview")
    existing_data = pd.read_excel(EXCEL_FILE)
    st.dataframe(existing_data.tail(10))  # Show last 3 entries

    # Download button
    st.download_button(
        label="Download Full Data",
        data=pd.read_excel(EXCEL_FILE).to_csv(index=False).encode("utf-8"),
        file_name="user_data.csv",
        mime="text/csv"
    )
if(option1=='create list'):
    # Streamlit interface
    st.title("👷 Manpower Management System")
    st.subheader("Add Workers")

    # Input form to add workers
    with st.form("add_worker"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Worker Name', key='new_name')
        with col2:
            work_type = st.selectbox(
                'Type of Work',
                options=['supervisior', 'skilled', 'semiskilled'],
                key='new_work'
            )

        add_submitted = st.form_submit_button("➕ Add Worker")

        if add_submitted:
            if not name:
                st.error("Please enter a name")
            else:
                # Create new entry DataFrame
                new_entry = pd.DataFrame([[name, work_type]],
                                         columns=['name', 'type of work'])

                # Append to existing data
                man_power = pd.concat([man_power, new_entry], ignore_index=True)

                # Save to Excel
                man_power.to_excel(EXCEL_FILE, index=False)
                st.success(f"✅ Added {name} ({work_type}) to workforce!")
                st.rerun()

if(option1=='delete list'):
    # Delete interface
    st.title("Current Workforce")
    st.subheader("Select workers to remove:")

    # Add selection checkbox to dataframe
    man_power['Select'] = False
    edited_df = st.data_editor(
        man_power,
        column_config={
            "Select": st.column_config.CheckboxColumn(required=True),
            "name": "Worker Name",
            "type of work": "Job Type"
        },
        hide_index=True,
        use_container_width=True
    )

    # Delete selected workers
    if st.button("🗑️ Delete Selected", type="primary"):
        if edited_df['Select'].sum() > 0:
            # Filter out selected rows
            man_power = edited_df[~edited_df['Select']].drop(columns=['Select'])

            # Save to Excel
            man_power.to_excel(EXCEL_FILE, index=False)
            st.success(f"✅ Removed {edited_df['Select'].sum()} worker(s)")
            st.rerun()
        else:
            st.warning("No workers selected")

    # Display current workforce without checkboxes
    st.divider()
    st.subheader("Current Workforce Overview")
    st.dataframe(man_power.drop(columns=['Select'], errors='ignore'),
                 use_container_width=True,
                 hide_index=True)
