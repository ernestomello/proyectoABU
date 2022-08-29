import { PersonalDataComponent } from '@profile/personal-data/personal-data.component';
import { Component, Input, OnInit, Output, ViewChild } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  idSocio:number = 2;

  @ViewChild(PersonalDataComponent, {static: true}) child! : PersonalDataComponent;

  constructor() { }

  ngOnInit() {
     this.child.idSocio = this.idSocio;
  }

}
