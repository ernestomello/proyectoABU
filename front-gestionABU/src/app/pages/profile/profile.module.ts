import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProfileRoutingModule } from "./profile.routing.module";

import { ProfileComponent } from "./profile.component";
import { AcademicDataModule } from './academic-data/academic-data.module';
import { PersonalDataModule } from './personal-data/personal-data.module';

@NgModule({
  declarations: [
    ProfileComponent,
  ],
  imports: [
    CommonModule,
    ProfileRoutingModule,
    PersonalDataModule,
    AcademicDataModule,
  ],
  exports: [
  ]
})
export class ProfileModule { }
