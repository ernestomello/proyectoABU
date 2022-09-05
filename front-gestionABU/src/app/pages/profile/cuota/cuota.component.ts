import { GenerarCuotaComponent } from './../generar-cuota/generar-cuota.component';
import { CuotaInterface } from './../../../shared/models/cuota.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { MatDialog } from '@angular/material/dialog';

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
  public generar_cuota_socio: string = 'Todos';

  constructor(
    private _profileService: ProfileService,
    public generar_cuota: MatDialog
    ) { }


  ngOnInit(): void {
    Promise.resolve().then(() => {
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
    });
  }

  buscador(): void {
    this.generar_cuota_socio = "Todos";
    // Busco lo que el usuario ingreso
    this.resultado_busqueda  = this.cuotas.filter(
      cuota =>
      cuota.nombre_socio.toLocaleLowerCase().
      indexOf(this.buscar.toLocaleLowerCase()) > -1
    ) ;
    // Me quedo con los ID de los socios encontrados en la busqueda
    const id_cuotas = this.resultado_busqueda.map(({id_socio}) => id_socio);

    if (this.resultado_busqueda.length === 0) {
      this.resultado_busqueda = this.cuotas;
    }
    // Compruebo si todsos los ID del resultado de la busqueda son iguales
    const unico = id_cuotas.filter((id_cuota, posicion, id_cuotas) =>{
      return posicion === id_cuotas.indexOf(id_cuota)
    })

    if (unico.length === 1) {
      this.generar_cuota_socio = this.resultado_busqueda[0].nombre_socio;
    }
  }

  generarCuota() {
    const dialogRef = this.generar_cuota.open(GenerarCuotaComponent);
    let fecha_desde = "";
    let fecha_hasta = "";

    dialogRef.afterClosed().subscribe(result => {
      fecha_desde = result.start.value?.format();
      fecha_hasta = result.end.value?.format();
    });


    // this._profileService.generarCuotaSocio().subscribe(() => {

    // });

  }


}
