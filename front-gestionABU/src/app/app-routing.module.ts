import { ListPersonalDataComponent } from './pages/profile/personal-data/list-personal-data/list-personal-data.component';
import { CheckLoginGuard } from '@shared/guars/check-login.guard';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [

  { path: 'admin', loadChildren: () => import('@admin/admin.module').then(m => m.AdminModule) },
  { path: 'socios', component:ListPersonalDataComponent,  loadChildren: () => import('@profile/personal-data/personal-data.module').then(m => m.PersonalDataModule) },
  // { path: 'socios', loadChildren: () => import('@profile/personal-data/personal-data.module').then(m => m.PersonalDataModule) },
  { path: 'cuotas', loadChildren: () => import('@profile/cuota/cuota.module').then(m => m.CuotaModule) },
  // { path: 'generar-cuotas', loadChildren: () => import('@profile/cuota/cuota.module').then(m => m.CuotaModule) },
  // { path: 'login', loadChildren: () => import('@auth/login/login.module').then(m => m.LoginModule), canActivate: [CheckLoginGuard] },
  { path: 'login', loadChildren: () => import('@auth/login/login.module').then(m => m.LoginModule)},
  { path: 'perfil', loadChildren: () => import('@profile/profile.module').then(m => m.ProfileModule) },
  { path: 'notFound', loadChildren: () => import('@pages/not-found/not-found.module').then(m => m.NotFoundModule) },
  { path: 'generar-cuota', loadChildren: () => import('@pages/profile/generar-cuota/generar-cuota.module').then(m => m.GenerarCuotaModule) },
  { path: '**', redirectTo:'', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
