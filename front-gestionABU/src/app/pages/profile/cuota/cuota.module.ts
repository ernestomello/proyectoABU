import { CuotaRoutesModule } from './cuota.routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CuotaComponent } from './cuota.component';



@NgModule({
  declarations: [
    CuotaComponent
  ],
  imports: [
    CommonModule,
    CuotaRoutesModule
  ]
})
export class CuotaModule { }
