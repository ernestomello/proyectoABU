import { PersonalResponse } from '@app/shared/models/persona.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';

@Component({
  selector: 'app-personal-data',
  templateUrl: './personal-data.component.html',
  styleUrls: ['./personal-data.component.css', '../profile.component.css']
})
export class PersonalDataComponent implements OnInit {

  @Input() id_socio: number = 0;
  @Input() person: PersonalResponse = {} as PersonalResponse;

  constructor(private _profileService: ProfileService) { }

  ngOnInit(): void {
    // Si no vienen personas que mande el componente padre busco la persona por this.idSocio
    if ( Object.keys(this.person).length === 0) {
      this._profileService.getPersonalData(this.id_socio).subscribe((response) => {
        this.person = response;
      });
    }
  }

}
