import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from "@angular/forms";
import IUser from 'src/app/models/user.models';
import { AuthService } from 'src/app/services/auth.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

constructor(
  private auth: AuthService,
  ) { }

  inSubmission = false

    name = new FormControl('',[
      Validators.required,
      Validators.minLength(3),
    ])
    email = new FormControl('',[
      Validators.required,
      Validators.email,
    ])
    age = new FormControl <number | null > (null,[
      Validators.nullValidator,
      Validators.required,
      Validators.min(18),
      Validators.max(120)
    ])
    password = new FormControl('',[
      Validators.pattern('[a-zA-Z0-9 ]*')
    ])
    confirm_password = new FormControl('',[
      Validators.required
    ])
    phoneNumber= new FormControl('',[
      Validators.required,
      Validators.minLength(13),
      Validators.maxLength(13)
    ])
  

  registerForm = new FormGroup({
    name: this.name,
    email: this.email,
    age: this.age,
    password: this.password,
    confirm_password: this.confirm_password,
    phoneNumber: this.phoneNumber
  })

  showAlert = false
  alertMsg = 'Please wait while your account is being created.'
  alertColor = 'blue'

  async register() {
    this.showAlert = true
    this.alertMsg = 'Please wait while your account is being created.'
    this.alertColor = 'blue'
    this.inSubmission = true

    //const {email, password} = this.registerForm.value

    try {
      await this.auth.createUser(this.registerForm.value as IUser)
    }
    catch (err) {
      console.error(err)

      this.alertMsg = 'An unexpected Error Occured, Please try again later'
      this.alertColor = 'red'
      this.inSubmission = false
      return
    }  

    this.alertMsg = 'Success! You have created the ACCOUNT'
    this.alertColor = 'green'
  }

}