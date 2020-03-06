import model
import pandas as pd 

import re    
import utils
import logging

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
    
    # add people that this meetups was their first time in DSPT meetups
    missing_df = first_timmers(members_df, attendees_df, columns)
    members_df = pd.concat([members_df, missing_df], ignore_index=True)

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

def first_timmers(members_df, attendees_df, columns):
    missing_ids = [int(x) for x in attendees_df["meetup_user_id"].values.astype(str)
    if x not in members_df["meetup_user_id"].values]
    len_missing = len(missing_ids)

    filter_missing = attendees_df["meetup_user_id"].apply(lambda x: True if x in missing_ids else False)
    tmp_df = attendees_df[filter_missing].copy()

    missing_df = pd.DataFrame()
    last_ordem = members_df["ordem"].values[-1]
    new_ordem = [x + int(last_ordem) for x in range(1, len_missing +1)]

    missing_df['ordem'] = new_ordem
    missing_df['meetup_user_id'] = tmp_df['meetup_user_id'].values.astype('int64')
    missing_df['member_name'] = tmp_df['member_name'].values
    missing_df['attended'] = ['X'] * len_missing

    missing_df.columns = columns
    return missing_df
    

if __name__ == "__main__":
    process_presences()