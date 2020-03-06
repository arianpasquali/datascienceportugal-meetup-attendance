# Data Science Portugal Meetup Attendance utilities

Utilities to handle meetup attendance

### Requirements

* [Python 3.7](https://www.python.org/)
* [Mozilla geckodriver](https://github.com/mozilla/geckodriver/)

## Installation

We recommend installing your requirements using virtualenv or anaconda. In order to install all python requirements:

```sh
pip install -r requirements.txt
```

### Using Anaconda

To create the environment with all the needed dependencies:

```sh
conda-env create -f requirements_conda.yaml
```

An then activate the environment when you want to use the tool:

```sh
conda activate meetup_attendance
```

## Load event attendance

In order to load event attendees:

```sh
python load_attendees.py --help
Usage: load_attendees.py [OPTIONS]

Options:
  -e, --event_url TEXT
```

Example loading attendees from event https://www.meetup.com/datascienceportugal/events/249301603 :

```sh
python load_attendees.py --event_url https://www.meetup.com/datascienceportugal/events/249301603

Loading attendees from Meetup Event
Fetching data from url https://www.meetup.com/datascienceportugal/events/249301603/attendees
Reading attendees ...
Exporting results to 249301603_attendees.csv
Success!
```

If a pop-up shows just close it, no actions needed.

## Assign attendance data

```sh
python assign_attendance.py --help
Usage: assign_attendance.py [OPTIONS]


Options:
  -d, --dspt-spreadsheet-filepath PATH
  -m, --meetup-attendees-filepath PATH
```


You need to download 'Lista de Presenças.xlsx' from our DSPT drive. Example assigning attendance data from our previous event:

```sh
python assign_attendance.py -d gdrive_dspt_presencas.xlsx -m 249301603_attendees.csv

Loading DSPT spreadsheet data
Loading Meetup.com attendees
Persisting attendance data into DSPT spreadsheet gdrive_dspt_presencas.xlsx
Check sheet 'TempPresenças' at gdrive_dspt_presencas.xlsx
```

That's it. 
Check the new temp sheet created (in the original spread sheet that you provided as input) and validate who attended the meetup.
You only have to add the last column from this temp sheet for the specific meetup. For first time participants you also have to add the name and meetup link information.

Please use with caution! Work in offline versions of the file and always confirm the changes you did before merging to the online file!!!
## Meta

arianpasquali@datascienceportugal.com

Distributed under the GPL license. See ``LICENSE`` for more information.

[https://github.com/arianpasquali/datascienceportugal-meetup-attendance](https://github.com/arianpasquali/datascienceportugal-meetup-attendance/)

## Contributing

1. Fork it (<https://github.com/arianpasquali/datascienceportugal-meetup-attendance/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
