import { LoginComponent } from '@auth/login/login.component';

import { HeaderComponent } from '@shared/components/header/header.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'admin', component: HeaderComponent },
  { path: 'login', component: LoginComponent },
  { path: 'notFound', loadChildren: () => import('@pages/not-found/not-found.module').then(m => m.NotFoundModule) },
  { path: 'admin', loadChildren: () => import('@admin/admin.module').then(m => m.AdminModule) },
  { path: 'login', loadChildren: () => import('@auth/login/login.module').then(m => m.LoginModule) },
  { path: '**', redirectTo:'', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
