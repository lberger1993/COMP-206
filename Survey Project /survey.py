#!/usr/bin/env python 
#!/usr/bin/python

import cgi 
import cgitb; cgitb.enable()

f = open ('takesurvey.html', 'w')

#uses survey.ssv file to display the <form> 

message = """<html> 

<head>
<title> Scripting Seagulls Survey Site </title>
<style type= "text/css">
h1{color: #000000; font: 250% Verdana, sans-serif;}
p{color: #000000; font: 75% Verdana, sans-serif; text-transform: lowercase;}
</style>
<link rel= "stylesheet" type= "text/css" href="ssss.css">
</head>
<body>
	<div id= "links"> 
	<a href= [insert link]> Login </a> <br>
	<a href= [insert link]> Create Account </a> <br>
	<a href= [insert link]> Fill Out Existing Survey </a> <br>
	<a href= [insert link]> Home </a> <br>
</div>


<!--Hyperlink from login page--> 

<div id="top">
<h1>Scripting Seagulls Survey Site.com</h1>
	<p>A place to gather and share data!</p>
</div>

<div id="content">
<h1> 
	<center> 
		<strong> CONTRA-CONTRA-CONTRA </strong> </br>  <u> controversies </u> 
	</center>
</h1>
<!--Questions and 4 radio buttons --> 
<p1> 
	
		 1. The moon-landing by the Americans in 1969 happened despite questionable motivation during the cold-war
	<form method = "get" action="survey.ssv">> 
		<input type="radio" name="answer" value="Strongly agree">Strongly Agree</br> 
		<input type="radio" name="answer" value="Agree">Agree</br> 	
		<input type="radio" name="answer" value="Disagree">Disagree</br>   
		<input type="radio" name="answer" value="Disagree Strongly">Disagree Strongly</br>   

	</br> 
</p1>

<p2> 
	
		 2.  The Sasquatch is alive and breathing. In fact, he was spotted in Mont Tremblont yesterday 
	
		<input type="radio" name="answer" value="Strongly agree">Strongly Agree</br> 
		<input type="radio" name="answer" value="Agree">Agree</br> 	
		<input type="radio" name="answer" value="Disagree">Disagree</br>   
		<input type="radio" name="answer" value="Disagree Strongly">Disagree Strongly</br>   

	</br> 
</p2>

<p3> 
	
	     3. Rob Ford is innocent. He was forced to use crack.	
	
		
		<input type="radio" name="answer" value="Strongly agree">Strongly Agree</br> 
		<input type="radio" name="answer" value="Agree">Agree</br> 	
		<input type="radio" name="answer" value="Disagree">Disagree</br>   
		<input type="radio" name="answer" value="Disagree Strongly">Disagree Strongly</br>   
	
	</br> 
</p3>
<p4> 
		4. Lee Harvey Oswald is innocent of killing JFK.  	
	
		<input type="radio" name="answer" value="Strongly agree">Strongly Agree</br> 
		<input type="radio" name="answer" value="Agree">Agree</br> 	
		<input type="radio" name="answer" value="Disagree">Disagree</br>   
		<input type="radio" name="answer" value="Disagree Strongly">Disagree Strongly</br>   

	</br> 
</p4>
<p5> 
		5. Obama was born in Kenya and is therefore illegally president of the United States.  	
	
	
		<input type="radio" name="answer" value="Strongly agree">Strongly Agree</br> 
		<input type="radio" name="answer" value="Agree">Agree</br> 	
		<input type="radio" name="answer" value="Disagree">Disagree</br>   
		<input type="radio" name="answer" value="Disagree Strongly">Disagree Strongly</br>   
	</form>

	</br> 
</p5>

</div>
</body>
</html>"""

f.write(message)
f.close()