# Data Science Portugal Meetup Attendance utilities

Utilities to handle meetup attendance

### Requirements

* [Python 3.7](https://www.python.org/)
* [Mozilla geckodriver](https://github.com/mozilla/geckodriver/)

## Installation

We recommend install your requirements using virtualenv or anaconda. In order to install all python requirements:

```sh
pip install -r requirements.txt
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

## Assign attendance data

```sh
python assign_attendance.py --help
Usage: assign_attendances.py [OPTIONS]

Options:
  -d, --dspt-spreadsheet-filepath PATH
  -m, --meetup-attendees-filepath PATH
```


You need to download 'Lista de Presenças.xlsx' from our DSPT drive. Example assigning attendance data from our previous event:

```sh
python assign_attendances.py -d gdrive_dspt_presencas.xlsx -m 249301603_attendees.csv

Loading DSPT spreadsheet data
Loading Meetup.com attendees
Persisting attendance data into DSPT spreadsheet dspt_presencas.xlsx
Check sheet 'TempPresenças' at dspt_presencas.xlsx
```

That's it. 
Check the temp sheet created and validate who attended the meetup. Don't forget to remove it when you finish.

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
