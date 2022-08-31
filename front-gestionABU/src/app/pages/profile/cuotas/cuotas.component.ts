import { CuotaInterface } from '../../../shared/models/cuota.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';

@Component({
  selector: 'app-cuota',
  templateUrl: './cuotas.component.html',
  styleUrls: ['./cuotas.component.css', '../profile.component.css']
})
export class CuotaComponent implements OnInit {

  public cuota: CuotaInterface = {} as CuotaInterface;
  @Input() idSocio: number = 0;

  constructor(private _profileService: ProfileService) { }

  ngOnInit(): void {
    console.log("FUNCIONA");

    // this._profileService.getCuotas(this.idSocio).subscribe((response) => {
    //   this.cuota = response;
    // });

  }

}
