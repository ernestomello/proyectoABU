import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PersonalDataRoutingModule } from './personal-data-routing.module';
import { PersonalDataComponent } from './personal-data.component';
import {MatListModule} from '@angular/material/list';
import {MatCardModule} from '@angular/material/card';


@NgModule({
  declarations: [
    PersonalDataComponent
  ],
  imports: [
    CommonModule,
    PersonalDataRoutingModule,
    MatCardModule,
    MatListModule
  ],
  exports:[
    PersonalDataComponent
  ]
})
export class PersonalDataModule { }
