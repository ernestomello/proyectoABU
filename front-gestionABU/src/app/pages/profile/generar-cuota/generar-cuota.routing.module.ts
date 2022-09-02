import { GenerarCuotaComponent } from './generar-cuota.component';
import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';

const routes: Routes = [{ path:'', component: GenerarCuotaComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class GenerarCuotaRoutesModule {}
