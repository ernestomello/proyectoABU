import { CuotaRoutesModule } from './cuota.routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CuotaComponent } from './cuota.component';

import { MaterialModule } from '@app/material.module';
import { ListCuotaComponent } from './list-cuota/list-cuota.component';

@NgModule({
  declarations: [
    CuotaComponent,
    ListCuotaComponent
  ],
  imports: [
    CommonModule,
    CuotaRoutesModule,
    MaterialModule
  ],
  exports:[
    CuotaComponent
  ]
})
export class CuotaModule { }
