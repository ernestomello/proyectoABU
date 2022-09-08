import { PersonalDataComponent } from '@profile/personal-data/personal-data.component';
import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  id_socio:number = 2;

  @ViewChild(PersonalDataComponent, {static: true}) personalDataComponent : PersonalDataComponent = {} as PersonalDataComponent;

  constructor() { }

  ngOnInit() {
     this.personalDataComponent.id_socio = this.id_socio;
  }

}
