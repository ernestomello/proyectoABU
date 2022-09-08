import { Component, OnInit } from '@angular/core';
import { PersonalResponse } from '@app/shared/models/persona.interface';
import { ProfileService } from '../../profile.service';

@Component({
  selector: 'app-admin-personal-data',
  templateUrl: './list-personal-data.component.html',
  styleUrls: ['./list-personal-data.component.css']
})
export class ListPersonalDataComponent implements OnInit {

  public persons: PersonalResponse [] =  new Array();

  constructor(private _profileService: ProfileService) { }

  ngOnInit(): void {
    this._profileService.getSocios().subscribe((response) => {
      this.persons = response;
    });
  }

}
