# Ezdust
Second-Year End Project, 2023  
Software and Knowledge Engineering, Faculty of Engineering, Kasetsart University

### List of members
* Napasorn Tevarut  (6510545519)
* Thorung Bunkaew   (6510545454)

### Project overview and features
Our project addresses the critical issue of air pollution in Bangkok by focusing on indoor air quality. Given the escalating concerns about pollution's impact on health, we aim to assess and improve the air inside homes and buildings. Through our research, we seek to empower individuals to take proactive steps towards creating healthier indoor environments, contributing to overall well-being and sustainability.  

Our web application has 3 main features.
* Users can search the district that they want to see the details information by searching district’s name in the search box or selecting the district from map directly and they can switch map mode into Indoor air quality map mode. After users select the district that they want to see the details, it will show the detail that consists of district’s name, outdoor air quality, outdoor temperature, outdoor humidity, indoor air quality from analytics, and graph that compare indoor and outdoor air quality over time.
* Users can predict the indoor air quality by themselves by entering their current district’s name, place type, and temperature.
* Our web application provides the API for both indoor and outdoor air quality, created by using Djangorest framework.

### Required libraries and tools
Required Python and Django packages are listed in [requirements.txt](./requirements.txt).

### Installation the Application
Read and follow the instructions in [Installation the Application](Installation.md).

### Running the Application

1. Start the server in the virtual environment. <br>
  Activate the virtualenv for this project
   * On Windows:
   ``` 
   venv\Scripts\activate
   ```
   * On macOS and Linux:
   ``` 
   source venv/bin/activate
   ```
   Start the django server:
   ```
   cd ezdust
   python manage.py runserver
   ```
   This starts a web server listening on port 8000.

2. You should see this message printed in the terminal window:
   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```
   If you get a message that the port is unavailable, then run the server on a different port (1024 thru 65535) such as:
   ```
   python manage.py runserver 12345
   ```

2. In a web browser, navigate to <http://localhost:8000>

3. To stop the server, press CTRL-C in the terminal window. Exit the virtual environment by closing the window or by typing:
   ```
   deactivate
   ```
