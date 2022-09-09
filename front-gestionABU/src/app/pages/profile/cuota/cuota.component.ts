import { CuotaInterface } from './../../../shared/models/cuota.interface';
import { Component, Input, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';
import { UntypedFormBuilder, UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-cuota',
  templateUrl: './cuota.component.html',
  styleUrls: ['./cuota.component.css']
})
export class CuotaComponent implements OnInit {

  @Input() resultado_busqueda: CuotaInterface[] = [] ;
  @Input() metodos: any = [];
  @Input() id_socio: number = 0;

  public datos_pago: UntypedFormGroup = this.initFormPago();

  constructor(
    private _profileService: ProfileService,
    private _fb: UntypedFormBuilder
    ) {}

  ngOnInit(): void {
    if (this.resultado_busqueda.length === 0 && this.id_socio !== 0) {
      this._profileService.getCuotasSocio(this.id_socio).subscribe((cuotas) =>{
        this.resultado_busqueda = Object.values (cuotas);
        console.log(this.resultado_busqueda);
      });
    }
  }

  pagar(id_cuota:number,id_socio:number): void{
    this.datos_pago.get('id_cuota')?.setValue(id_cuota);
    this.datos_pago.get('id_socio')?.setValue(id_socio)
    const form_datos_pago = this.datos_pago.value;

    this._profileService.pagarCuota(form_datos_pago).subscribe((response) => {
      console.log("RESPONSE:");
      console.log(response);
    });
    this.datos_pago.reset();
  }

    // Inicializo el formulario de pago
    initFormPago():UntypedFormGroup {
      return this._fb.group({
        metodo_pago : new UntypedFormControl('', [Validators.required]),
        descripcion:  new UntypedFormControl('',),
        id_cuota:     new UntypedFormControl('',),
        id_socio:     new UntypedFormControl('',)
      });
    }








}
