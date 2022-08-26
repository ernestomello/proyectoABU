import { NgModule } from "@angular/core";
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatToolbarModule} from '@angular/material/toolbar';
import { MatSidenavModule} from '@angular/material/sidenav'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';


const modules = [
  MatCardModule,
  MatInputModule,
  MatButtonModule,
  MatIconModule,
  MatSnackBarModule,
  MatToolbarModule,
  MatSidenavModule,
  ReactiveFormsModule,
  FormsModule,
  MatProgressSpinnerModule
];

@NgModule({
  imports: modules,
  exports: modules,
})

export class MaterialModule {}
