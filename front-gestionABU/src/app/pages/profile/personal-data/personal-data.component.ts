import { PersonalResponse } from '@app/shared/models/persona.interface';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-personal-data',
  templateUrl: './personal-data.component.html',
  styleUrls: ['./personal-data.component.css', '../profile.component.css']
})
export class PersonalDataComponent implements OnInit {

  @Input() idSocio: number = 0;
  @Input() person: PersonalResponse = {} as PersonalResponse;

  constructor() { }

  ngOnInit(): void {
   if (this.person == null) {
    console.log("BUSCAR UNO");

   }

  }

}
