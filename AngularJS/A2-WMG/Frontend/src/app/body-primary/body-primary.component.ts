import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-body-primary',
  templateUrl: './body-primary.component.html',
  styleUrls: ['./body-primary.component.css']
})
export class BodyPrimaryComponent implements OnInit {

  constructor(
    public auth: AuthService
  ) { }

  user: any
  readuser: any

  ngOnInit(): void {
    this.auth.getUserState().subscribe (
      user => {
        this.user = user
      }
    )
    this.auth.getUser().subscribe((res)=> {

      this.readuser = res.data
      console.log(this.readuser)

    })
  }

  

}
