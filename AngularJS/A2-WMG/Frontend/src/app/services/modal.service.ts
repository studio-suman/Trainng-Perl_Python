import { Injectable } from '@angular/core';



//Creating Interface
interface IModal {
  id: string;
  visible: boolean;
}

@Injectable({
  providedIn: 'root'
})

//@Injectable()


export class ModalService {
  private modals: IModal[] = []

  constructor() { }

//Creating Register Function
register(id:string) {
  this.modals.push({
    id,
    visible: false
  })
  //console.log(this.modals) //tracking the ID system
}

unregister(id:string) {
  this.modals = this.modals.filter(
    element => element.id !== id
  )
}

// Checking If Modal is open or not
  isModalOpen(id:string) : boolean {
    //wrapping Boolean for conversion '!!'
    return !!this.modals.find(element => element.id === id)?.visible
  }
//Toggle 
  toggleModal(id:string) {
    const modal = this.modals.find(element => element.id === id)
    if(modal) {
      modal.visible = !modal.visible
    }
  }
}

