import webapp2
import valid
import escape

form = """
<form method="post">
	<b>Signup</b>
	<br>
	
	<label> Username
		<input type="text" name="username" value="%(username)s">
		<div style="color: red">%(blank_username)s</div>
	</label>
	<br>
	
	<label> Password		
		<input type="text" name="password" value="%(password)s">
		<div style="color: red">%(blank_password)s</div>
	</label>
	<br>
	
	<label> Verify Password
		<input type="text" name="v_pass" value="%(v_pass)s">
		<div style="color: red">%(not_match_password)s</div>
	</label>
	<br>
	
	<label>	Email (optional)
		<input type="text" name="email" value="%(email)s">
		<div style="color: red">%(invalid_email)s</div>
	</label>
	
	
	<br>
	<br>
	<input type="submit">
</form>
""" 

		
class MainPage(webapp2.RequestHandler):
	def write_form(self, blank_username="", blank_password="", not_match_password="", invalid_email="",
					username="", password="", v_pass="", email=""):
		self.response.write(form % {"blank_username": blank_username,
									"blank_password": blank_password,
									"not_match_password": not_match_password,
									"invalid_email": invalid_email,
									"username": escape.escape_html(username),
									"password": escape.escape_html(password),
									"v_pass": escape.escape_html(v_pass),
									"email": escape.escape_html(email)})
	
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.write(form)
		self.write_form()
	
	def post(self):
		user_username = self.request.get("username")
		user_password = self.request.get("password")
		user_v_pass = self.request.get("v_pass")
		user_email = self.request.get("email")
		
		username = user_username
		password = user_password
		v_pass = user_v_pass
		email = user_email
		
		if (username == "") and (password == ""):
			#self.response.write(form)
			self.write_form("Invalid username", "Invalid password", "", "", user_username, user_password, user_v_pass, user_email)
		elif (password == ""):
			self.write_form("", "Invalid password", "", "", user_username, user_password, user_v_pass, user_email)
		
		elif (username == "") and (password != v_pass):
			self.write_form("Invalid username", "", "Password did not match", "", user_username, user_password, user_v_pass, user_email)
		elif (password != v_pass):
			self.write_form("", "", "Password did not match", "", user_username, user_password, user_v_pass, user_email)
		elif not (email):
			self.write_form("", "", "", "Invalid e-mail", user_username, user_password, user_v_pass, user_email)
		else:
			self.redirect("/welcome")
		"""
		if not (password == v_pass):
			self.write_form("password did not match", user_username, user_password, user_v_pass, user_email)
			if (email != ""):
				if not (email):
					self.write_form("Invalid e-mail", user_username, user_password, user_v_pass, user_email)
		"""
		
			
	
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Welcome!")

		
application = webapp2.WSGIApplication([
    ('/', MainPage),
	('/welcome', WelcomeHandler)
], debug=True)

#('/testform', Testhandler), #si deve creare questo handler perche' questo path non esiste nel web
