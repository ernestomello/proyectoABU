import { ProfileService } from './../profile.service';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-personal-data',
  templateUrl: './personal-data.component.html',
  styleUrls: ['./personal-data.component.css', '../profile.component.css']
})
export class PersonalDataComponent implements OnInit {

  public nombre: string = '';
  public apellido_paterno: string = '';
  public apellido_materno: string = '';
  public fecha_nacimiento: string = '';
  public direccion: string = '';
  public telefono: string = '';
  public celular: string = '';
  public correo: string = '';


  constructor(private _profileService: ProfileService) { }

  @Input() idSocio: number = 0;

  ngOnInit(): void {
    this._profileService.getPersonalData(this.idSocio).subscribe((response: any) => {
      this.nombre = response['nombre'];
      this.apellido_paterno = response['apellido_paterno'];
      this.apellido_materno = response['apellido_materno'];
      this.fecha_nacimiento = response['fecha_nacimiento'];
      this.direccion = response['direccion'];
      this.telefono = response['telefono'];
      this.celular = response['celular'];
      this.correo = response['correo'];

    });
  }

}
