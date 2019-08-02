# Data Science Portugal Meetup Attendance utilities

Utilities to handle meetup attendance

### Requirements

* [Python 3.7](https://www.python.org/)
* [Mozilla geckodriver](https://github.com/mozilla/geckodriver/)

## Installation

We recommend install your requiriments using virtualenv or anaconda. In order to install all python requirements:

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

Exemple loading attendees from event https://www.meetup.com/datascienceportugal/events/249301603 :

```sh
python load_attendees.py --event_url https://www.meetup.com/datascienceportugal/events/249301603
```

## Testing
To run tests you can use [pytest](https://pytest.org):

```sh
pytest
```

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