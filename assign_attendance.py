import model
import pandas as pd 

import re    
import utils
import logging

import pandas as pd
import click

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('--dspt-spreadsheet-filepath', "-d", type=click.Path(exists=True))
@click.option('--meetup-attendees-filepath', "-m", type=click.Path(exists=True))
def process_presences(dspt_spreadsheet_filepath, meetup_attendees_filepath):
       
    if(not dspt_spreadsheet_filepath or not meetup_attendees_filepath):
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
        
    click.echo("Loading DSPT spreadsheet data")
    xls = model.PresenceSpreadsheet(dspt_spreadsheet_filepath) 
    xls.load() 
    xls.read_members()
    

    click.echo("Loading Meetup.com attendees")
    attendees_df = pd.read_csv(meetup_attendees_filepath)

    members_df = pd.DataFrame(xls.members)

    # check each member attendance
    members_df["attended"] = members_df["meetup_user_id"].apply(lambda x: isAttendee(x, attendees_df)) 

    # select columns
    columns = ["ordem", "meetup_user_id", "name", "attended"]
    members_df = members_df[columns]
    # debug
    # members_df.to_csv("presencas.csv", index=False)

    click.echo("Persisting attendance data into DSPT spreadsheet {}" .format( dspt_spreadsheet_filepath))
    tmpSheet = xls.wb.create_sheet(title="TempPresenças")
    for column_id, column_item  in enumerate(columns):
        tmpSheet.cell(column=column_id + 1, row=1, value=column_item)

    for index, row in members_df[columns].iterrows():
        for column_id, column_name  in enumerate(columns):
            tmpSheet.cell(column=column_id + 1, row=index + 2, value=row[column_name])

    xls.wb.save(filename = dspt_spreadsheet_filepath)

    click.echo("Check sheet 'TempPresenças' at {}".format(dspt_spreadsheet_filepath) )

def isAttendee(x, attendees_df): 
    for u_id in attendees_df["meetup_user_id"].values: 
        if(str(u_id) == str(x)): 
            return "X"
    return ""

if __name__ == "__main__":
    process_presences()