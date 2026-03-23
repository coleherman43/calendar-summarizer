import pandas as pd
import csv
from icalendar import Calendar

# Inspiration: https://medium.com/@bobbie.wxy/convert-calendar-ics-file-to-csv-file-eac0e7c84da0
def ics_to_csv():
    # Calendar path vars (create new one for csv)
    ics_path = 'cole_calendar.ics'
    csv_path = 'calendar.csv'

    # Write csv to create it
    csv_file = open(csv_path, 'w', newline='', encoding='utf-8')

    # Create header
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Subject', 'Start Time', 'End Time', 'Description'])

    # Read iCal
    with open(ics_path, 'rb') as ics_file:
        cal = Calendar.from_ical(ics_file.read())
        for event in cal.walk('VEVENT'):
            subject = event['SUMMARY']
            start_time = event['DTSTART'].dt
            if 'DTEND' in event:
                end_time = event['DTEND'].dt
            else:
                end_time = start_time
            if 'DESCRIPTION' in event:
                description = event['DESCRIPTION']
            else:
                description = None
            csv_writer.writerow([subject, start_time, end_time, description])
    csv_file.close()

def import_calendar_data():
    df = pd.read_csv('calendar.csv')



def main():
    # Convert ics to csv - CLI tool or just file path in code?
    ics_to_csv()
    # Import data
    import_calendar_data()
    # Parse data

    # Preprocess data (ex. calculate length)

    # Group data by type / aggregate

    # Optional regex checks for keywords

    # TODO visualize with streamlit


    pass

if __name__ == "__main__":
    main()