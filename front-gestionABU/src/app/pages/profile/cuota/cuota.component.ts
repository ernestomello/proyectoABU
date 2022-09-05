import { GenerarCuotaComponent } from './../generar-cuota/generar-cuota.component';
import { CuotaInterface } from './../../../shared/models/cuota.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

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
    public generar_cuota: MatDialog,
    private _snackBar: MatSnackBar
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
    this.idSocio = 0;
    // Busco lo que el usuario ingreso
    this.resultado_busqueda  = this.cuotas.filter(
      cuota =>
      cuota.nombre_socio.toLocaleLowerCase().
      indexOf(this.buscar.toLocaleLowerCase()) > -1
    ) ;
    // Me quedo con los ID de los socios encontrados en la busqueda
    const id_cuotas = this.resultado_busqueda.map(({id_socio}) => id_socio);

    // Compruebo si todsos los ID del resultado de la busqueda son iguales
    const unico = id_cuotas.filter((id_cuota, posicion, id_cuotas) =>{
      return posicion === id_cuotas.indexOf(id_cuota)
    })
    // Si retorna un ID solo me quedo con el nombre y el id de ese socio
    if (unico.length === 1) {
      this.generar_cuota_socio = this.resultado_busqueda[0].nombre_socio;
      this.idSocio = this.resultado_busqueda[0].id_socio;
    }
  }

  generarCuota() {
    const dialogRef = this.generar_cuota.open(GenerarCuotaComponent);
    let fecha_desde: Date = new Date();
    let fecha_hasta: Date = new Date();

    // Muestro el modal para que eliga el rango de fecha que quiere
    dialogRef.afterClosed().subscribe(result => {
      fecha_desde = result.start.value?.format().slice(0, 10);
      fecha_hasta = result.end.value?.format().slice(0, 10);
      // Mando a generar la cuota
      this._profileService.generarCuotaSocio(this.idSocio, fecha_desde, fecha_hasta).subscribe((response: any) => {
        this._snackBar.open(response['Respuesta'], "OK", {
          duration: 5000
        });
      });
    // Actualizo las cuotas
    this._profileService.getCuotas().subscribe((response) => {
      this.cuotas = Object.values (response);
      this.resultado_busqueda = this.cuotas;
    });
    });
  }


}
