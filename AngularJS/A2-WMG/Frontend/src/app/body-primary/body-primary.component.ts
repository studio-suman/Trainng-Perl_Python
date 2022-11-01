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

  ngOnInit(): void {
    this.auth.getUserState().subscribe (
      user => {
        this.user = user
      }
    )
  }

}
