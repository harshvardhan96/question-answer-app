# Read me file for question-answer-app

1. The API code is present in the api.py file.
2. Demo.py file consists code for adding data to Redis client.
   
3. I tried hosting the solution on AWS, but during the step where I had to accept the requests from the user and route it to gunicorn, I was getting an error, namely, 
"systemctl Failed to get D-Bus connection." 

4. The Steps which needed to be followed further to expose the port are:
   - Run Nginx Webserver to accept and route request to Gunicorn.

5. I have uploaded a video of a demo which I recorded on my local machine. The link to it is as follows:

6. If you wish to run it on your local machine, install dependecies and then run the api.py file. You will need to use curl or Postman tool to send a post request to the running application. The sample JSON for the same should be as follows:

{
    "question": "updation_correction_in_pan_card"
}

7. It would return the information that has been stored in the redis database corresponding to this key.
