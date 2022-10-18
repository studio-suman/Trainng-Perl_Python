import { Component, OnInit } from '@angular/core';
import { ModalService } from '../services/modal.service';
import { AuthService } from '../services/auth.service';
import { AngularFireModule } from '@angular/fire/compat';


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

    user: any

  ngOnInit(): void {
    this.auth.getUserState().subscribe (
      user => {
        this.user = user
      }
    )
  }
 
  logout($event:Event) {
    $event.preventDefault()
    this.auth.logout();
  }

  openModal($event: Event) {
    $event.preventDefault()

    this.modal.toggleModal('auth')
  }

}
