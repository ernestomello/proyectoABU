import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AcademicDataComponent } from './academic-data.component';


import {MatListModule} from '@angular/material/list';
import {MatCardModule} from '@angular/material/card';



@NgModule({
  declarations: [
    AcademicDataComponent
  ],
  imports: [
    CommonModule,
    MatListModule,
    MatCardModule
  ],
  exports:[
    AcademicDataComponent
  ]
})
export class AcademicDataModule { }
