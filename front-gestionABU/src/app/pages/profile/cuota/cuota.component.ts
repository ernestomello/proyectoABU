import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { ProfileService } from '../profile.service';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-cuota',
  templateUrl: './cuota.component.html',
  styleUrls: ['./cuota.component.css']
})
export class CuotaComponent implements OnInit {

  // public cuotas: CuotaInterface = {} as CuotaInterface;
  public cuotas: any;
  @Input() idSocio: number = 0;

  disableSelect = new FormControl(false);


  constructor(private _profileService: ProfileService) { }

  ngOnInit(): void {
    if (this.idSocio > 0) {
      this._profileService.getCuotasSocio(this.idSocio).subscribe((response) => {
        this.cuotas = Object.values (response);
      });
    } else {
      this._profileService.getCuotas().subscribe((response) => {
        this.cuotas = Object.values (response);
      });
    }
  }

}
