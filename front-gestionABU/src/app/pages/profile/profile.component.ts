import { CuotaComponent } from './cuotas/cuotas.component';
import { PersonalDataComponent } from '@profile/personal-data/personal-data.component';
import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  idSocio:number = 2;

  @ViewChild(PersonalDataComponent, {static: true}) personalDataComponent : PersonalDataComponent = {} as PersonalDataComponent;
  @ViewChild(CuotaComponent, {static: true}) cuotaComponent : CuotaComponent = {} as CuotaComponent;

  constructor() { }

  ngOnInit() {
     this.personalDataComponent.idSocio = this.idSocio;
     this.cuotaComponent.idSocio = this.idSocio;
  }

}
