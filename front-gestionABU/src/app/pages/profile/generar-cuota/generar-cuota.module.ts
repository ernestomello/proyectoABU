import { GenerarCuotaRoutesModule } from './generar-cuota.routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GenerarCuotaComponent } from './generar-cuota.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { MaterialModule } from '@app/material.module';

@NgModule({
  declarations: [
    GenerarCuotaComponent
  ],
  imports: [
    CommonModule,
    GenerarCuotaRoutesModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    BrowserModule,

  ],
  exports:[
    GenerarCuotaComponent
  ]
})
export class GenerarCuotaModule { }
