import { PersonalResponse } from '@app/shared/models/persona.interface';
import { ProfileService } from './../profile.service';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-personal-data',
  templateUrl: './personal-data.component.html',
  styleUrls: ['./personal-data.component.css', '../profile.component.css']
})
export class PersonalDataComponent implements OnInit {

  public person: PersonalResponse = {} as PersonalResponse;
  @Input() idSocio: number = 0;

  constructor(private _profileService: ProfileService) { }

  ngOnInit(): void {
    this._profileService.getPersonalData(this.idSocio).subscribe((response) => {
      this.person = response;
    });
  }

}
