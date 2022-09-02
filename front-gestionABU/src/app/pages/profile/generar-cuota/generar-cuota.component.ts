import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';

const today = new Date();
const month = today.getMonth();
const year = today.getFullYear();

@Component({
  selector: 'app-generar-cuota',
  templateUrl: './generar-cuota.component.html',
  styleUrls: ['./generar-cuota.component.css']
})
export class GenerarCuotaComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  campaignOne = new FormGroup({
    start: new FormControl(new Date(year, month, 13)),
    end: new FormControl(new Date(year, month, 16)),
  });
  campaignTwo = new FormGroup({
    start: new FormControl(new Date(year, month, 15)),
    end: new FormControl(new Date(year, month, 19)),
  });

}
