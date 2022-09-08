import { Component, Input, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { CuotaInterface } from '@app/shared/models/cuota.interface';
import { GenerarCuotaComponent } from '../../generar-cuota/generar-cuota.component';
import { ProfileService } from '../../profile.service';

@Component({
  selector: 'app-list-cuota',
  templateUrl: './list-cuota.component.html',
  styleUrls: ['./list-cuota.component.css', '../cuota.component.css']
})
export class ListCuotaComponent implements OnInit {

  @Input() id_socio: number = 0;

  public buscar: string = '';
  public generar_cuota_socio: string = 'Todos';
  public resultado_busqueda: CuotaInterface[] = [] ;
  public cuotas: CuotaInterface[] = [] ;
  public metodos: any = [];

  constructor(
    public generar_cuota: MatDialog,
    private _profileService: ProfileService,
    private _snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {
    this.getCuotas();
    this._profileService.getMetodoPago().subscribe((metodos) => {
      this.metodos = metodos
    });
  }

  buscador(): void {
    this.generar_cuota_socio = "Todos";
    this.id_socio = 0;
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
      this.id_socio = this.resultado_busqueda[0].id_socio;
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
      this._profileService.generarCuotaSocio(this.id_socio, fecha_desde, fecha_hasta).subscribe((response: any) => {
        this._snackBar.open(response['Respuesta'], "OK", {
          duration: 5000
        });
        this.reset();
        this.getCuotas();
      });

    });
  }

  getCuotas():void{
    this._profileService.getCuotasSocio(this.id_socio).subscribe((cuotas) => {
      this.cuotas = Object.values (cuotas);
      this.resultado_busqueda = this.cuotas;
      console.log(this.resultado_busqueda );

    });
  }

  reset(){
    this.id_socio = 0;
    this.buscar = '';
  }

}
