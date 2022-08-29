import { CheckLoginGuard } from '@shared/guars/check-login.guard';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'perfil', loadChildren: () => import('@profile/profile.module').then(m => m.ProfileModule) },
  { path: 'admin', loadChildren: () => import('@admin/admin.module').then(m => m.AdminModule) },
  // { path: 'login', loadChildren: () => import('@auth/login/login.module').then(m => m.LoginModule), canActivate: [CheckLoginGuard] },
  { path: 'login', loadChildren: () => import('@auth/login/login.module').then(m => m.LoginModule)},

  { path: 'notFound', loadChildren: () => import('@pages/not-found/not-found.module').then(m => m.NotFoundModule) },
  { path: '**', redirectTo:'', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
