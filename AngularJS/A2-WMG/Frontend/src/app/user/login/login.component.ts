import { Component, OnInit } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  credentials = {
    email: "",
    password: ""
  }

  showAlert = false
  alertMsg = "Please wait while we log you in"
  alertColor = 'blue'
  inSubmission = false



  constructor(
    private auth: AngularFireAuth,
    ) { }

  ngOnInit(): void {
  }

  async login() {
    this.showAlert = true
    this.alertMsg = "Please wait while we log you in"
    this.alertColor = 'Blue'
    this.inSubmission = true
    console.log(this.credentials)
    

    try {
      await this.auth.signInWithEmailAndPassword(
        this.credentials.email, this.credentials.password)
        console.log(this.credentials)
    }
    catch (e) {
      this.inSubmission = false
      this.alertMsg = "An unexpected Error has occured! Please try again later"
      this.alertColor = 'red'

      console.log(e)

      return
    }

    this.alertMsg = "Success! You are now logged in!"
    this.alertColor = 'green'

  }

}
