# dog-breed-detection-service
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tabris2015/dog-breed-detection-service/)

## Install

Install pip:
```
sudo apt install python-pip
```

Install virtualenv globally:
```
sudo pip install virtualenv
```

Clone this repo:

```
git clone https://github.com/tabris2015/dog-breed-detection-service.git
cd dog-breed-detection-service
```

Create virtual environment:
```
virtualenv env
```
Activate virtual environment:
```
source env/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```

## Run local server
With virtual env activated:
```
python manage.py runserver
```

In a browser, enter to `http://127.0.0.1:8000/`, you will need to grant webcam permissions to the host
and then you will see a camera feed. For taking a snapshot and perform a detection on that, press
the button `Detect`, the neural network will process the image and may take several seconds. Once 
the detection is finished, the results are going to be shown below the button.


