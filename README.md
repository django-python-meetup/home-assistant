# Greenville Django Python Meetup

## Home Assistant Demo

We looked at a home automation system written in Python3 called Home Assistant.

[Intro Slides](https://raw.githubusercontent.com/django-python-meetup/home-assistant/master/hass_meetup_intro.pdf)

## Install

Make sure python3 is installed. I did this with the package manager called `homebrew`

To install Homebrew, open Terminal or your favorite OSX terminal emulator and run

`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

The script will explain what changes it will make and prompt you before 
the installation begins. Once you’ve installed Homebrew, insert the 
Homebrew directory at the top of your __PATH__ environment variable. You can 
do this by adding the following line at the bottom of your `~/.profile` file

`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`

Now, we can install Python 3:

`$ brew install python3`

Using virtualenvwrapper create a new virtual environment that uses python3:

```
$ mkvirtualenv --python=`which python3` home-assistant
```

Then install Home Assistent in the new virtualenv

`pip3 install homeassistant`

Once the install finishes, run home assistant

`hass --open-ui`

The `open-ui` flag tells home assistant to run the web server and launch 
a web browser pointed to the running server.

## Configure

In the demo we looked at how to work with the files in the `~/.homeassistant` folder
that is created by home assistant the first time it is run. The files in this repo
represent the configuration that was used for the switch demo.