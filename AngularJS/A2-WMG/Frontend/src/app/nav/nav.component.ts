import { Component, OnInit } from '@angular/core';
import { ModalService } from '../services/modal.service';
import { AuthService } from '../services/auth.service';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {


  constructor(
    public modal: ModalService,
    public auth: AuthService
    ) { 

    }

  ngOnInit(): void {
  }
 
  logout($event:Event) {
    $event.preventDefault()
    this.auth.logout();
  }

  openModal($event: Event) {
    $event.preventDefault()

    this.modal.toggleModal('auth')
  }

  userinfo = "Suman Saha"
}
