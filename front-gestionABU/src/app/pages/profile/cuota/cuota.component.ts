import { CuotaInterface } from './../../../shared/models/cuota.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-cuota',
  templateUrl: './cuota.component.html',
  styleUrls: ['./cuota.component.css']
})
export class CuotaComponent implements OnInit {

  // public cuotas: CuotaInterface = {} as CuotaInterface;
  public cuotas: CuotaInterface[] = [] ;
  public resultado_busqueda: CuotaInterface[] = [] ;
  @Input() idSocio: number = 0;
  public buscar: string = '';
  public generar_cuota: string = 'Todos';


  disableSelect = new FormControl(false);

  constructor(private _profileService: ProfileService) { }


  ngOnInit(): void {
    if (this.idSocio > 0) {
      this._profileService.getCuotasSocio(this.idSocio).subscribe((response) => {
        this.cuotas = Object.values (response);
        this.resultado_busqueda = this.cuotas;
      });
    } else {
      this._profileService.getCuotas().subscribe((response) => {
        this.cuotas = Object.values (response);
        this.resultado_busqueda = this.cuotas;
      });
    }
  }

  buscador(): void {
    this.generar_cuota = "Todos";
    this.resultado_busqueda  = this.cuotas.filter( cuota => cuota.importe == parseInt(this.buscar) ) ;
    if (this.resultado_busqueda.length == 0) {
      this.resultado_busqueda = this.cuotas;
    }
    const unico = this.resultado_busqueda.filter((cuota, posicion, cuotas) =>{ return posicion === cuotas.indexOf(cuota)})
    if (unico.length == 1) {
      this.generar_cuota = "BIEN";
    }
    console.log(this.resultado_busqueda)
  }

  generarCuota(): void {
    window.alert("GENERARA LA CUOA !!!!!")
  }


}
