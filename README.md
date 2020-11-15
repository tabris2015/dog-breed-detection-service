# dog-breed-detection-service
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tabris2015/dog-breed-detection-service/)

## Install
For installing, follow the steps:

  1. Install pip:
    ```
    sudo apt install python-pip
    ```
  3. Install virtualenv globally:
    ```
    sudo pip install virtualenv
    ```
  4. Clone this repo:
    ```
    git clone https://github.com/tabris2015/dog-breed-detection-service.git
    && cd dog-breed-detection-service
    ```
    
  5. Create virtual environment:
    ```
    virtualenv env
    ```
  6. Activate virtual environment:
    ```
    source env/bin/activate
    ```
  7. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Add localhost as secure on Chrome
In order to access to the webcam, you need to bypass Insecure Origins
block of Chrome for localhost. 
  1. In Chrome, go to `chrome://flags/#unsafely-treat-insecure-origin-as-secure`
  2. Find the Insecure origins treated as secure setting.
  3. Enable it.
  4. Enter `http://127.0.0.1:8000/`
  5. Restart Chrome
  
## Run local server
With virtual env activated:
```
python manage.py runserver
```

In a browser, enter to `http://127.0.0.1:8000/`, you will need to grant webcam permissions to the host
and then you will see a camera feed. For taking a snapshot and perform a detection on that, press
the button `Detect`, the neural network will process the image and may take several seconds. Once 
the detection is finished, the results are going to be shown below the button.


  



