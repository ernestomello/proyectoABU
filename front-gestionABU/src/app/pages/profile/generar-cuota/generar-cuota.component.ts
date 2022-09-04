import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

import { MomentDateAdapter } from '@angular/material-moment-adapter';
import { DateAdapter, MAT_DATE_FORMATS, MAT_DATE_LOCALE } from '@angular/material/core';
import { MatDatepicker } from '@angular/material/datepicker';
import * as _moment from 'moment';
import { Moment } from 'moment';

const moment = _moment;

// Formato que se mostrara la fecha
export const FORMAT_DATE = {
  parse: {
    dateInput: 'LL',
  },
  display: {
    dateInput: 'MM-YYYY',
    monthYearLabel: 'YYYY',
    dateA11yLabel: 'LL',
    monthYearA11yLabel: 'YYYY',
  },
};

@Component({
  selector: 'app-generar-cuota',
  templateUrl: './generar-cuota.component.html',
  styleUrls: ['./generar-cuota.component.css'],
  providers: [
    { provide: DateAdapter, useClass: MomentDateAdapter, deps: [MAT_DATE_LOCALE] },
    { provide: MAT_DATE_FORMATS, useValue: FORMAT_DATE },
  ],
})
export class GenerarCuotaComponent implements OnInit {

  // Fecha desde y hasta cuando quiere generar las cuotas
  start = new FormControl(moment());
  end = new FormControl(moment());
  minDate : Date = new Date();

  constructor( ) { }

  ngOnInit(): void {
  }

  setMonthAndYearStart(normalizedMonthAndYear: Moment, datepicker: MatDatepicker<Moment>) {
    const ctrlValue = this.start.value!;
    ctrlValue.month(normalizedMonthAndYear.month());
    ctrlValue.year(normalizedMonthAndYear.year());
    this.start.setValue(ctrlValue);
    // Seteo la fecha minima de la fecha de finalizacion como la fecha de inicio uso el operador ! para decir que la fecha no sera nula
    this.minDate = ctrlValue?.toDate()!;
    // Seteo la fecha de finalizacion como la fecha de inicio para que no haya errores
    this.end.setValue(moment(ctrlValue?.toDate()));
    datepicker.close();
  }

  setMonthAndYearEnd(normalizedMonthAndYear: Moment, datepicker: MatDatepicker<Moment>) {
    const ctrlValue = this.end.value!;
    ctrlValue.month(normalizedMonthAndYear.month());
    ctrlValue.year(normalizedMonthAndYear.year());
    this.end.setValue(ctrlValue);
    datepicker.close();
  }

}
